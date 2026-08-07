from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "CHECKSUM_SCOPE.json"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise ValueError(message)


def git_bytes(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], stderr=subprocess.STDOUT)


def safe_relative(value: str) -> str:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or value.startswith(".git/"):
        fail(f"Unsafe or non-tree path: {value!r}")
    return path.as_posix()


def read_manifest(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2 or not SHA256_RE.fullmatch(parts[0]):
            fail(f"Malformed manifest line {line_number}")
        relative = safe_relative(parts[1].lstrip("*").strip())
        if relative in result:
            fail(f"Duplicate manifest path: {relative}")
        result[relative] = parts[0]
    return result


def main() -> int:
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        if config.get("schema_version") != "checksum-scope.v1":
            fail("Unsupported checksum-scope schema_version")
        declaration = config["derived_git_tree_manifest"]
        commit = declaration["source_commit"]
        if not COMMIT_RE.fullmatch(commit):
            fail("Malformed source_commit")
        git_bytes("cat-file", "-e", f"{commit}^{{commit}}")
        expected_paths = git_bytes("ls-tree", "-r", "--name-only", commit).decode("utf-8").splitlines()
        expected_paths = [safe_relative(path) for path in expected_paths]
        manifest_path = ROOT / declaration["path"]
        entries = read_manifest(manifest_path)
        if len(entries) != declaration["entry_count"]:
            fail("Derived manifest entry count disagrees with CHECKSUM_SCOPE.json")
        if set(entries) != set(expected_paths) or len(expected_paths) != len(set(expected_paths)):
            fail("Derived manifest path set differs from the tagged Git tree")
        for relative in expected_paths:
            actual = hashlib.sha256(git_bytes("show", f"{commit}:{relative}")).hexdigest()
            if actual != entries[relative]:
                fail(f"Git-blob checksum mismatch: {relative}")
        print(f"PASS tagged Git-tree manifest: {len(entries)} blobs at {commit}")
        return 0
    except (OSError, KeyError, TypeError, UnicodeDecodeError, json.JSONDecodeError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
