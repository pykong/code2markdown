import sys

from pathlib import Path
from typing import Final
from subprocess import check_output

from pathspec import PathSpec

OUTPUT_FILE: Final[Path] = Path("comp.md")
PATTERNS_FILE: Final[str] = "patterns.list"
with open(PATTERNS_FILE, "r") as fh:
    SPEC: Final[PathSpec] = PathSpec.from_lines("gitwildmatch", fh)


def make_markdown(suffix: str, text: str) -> str:
    return f"'''{suffix}\n{text}\n'''"


def make_filetree(p: Path) -> str:
    cmd = f"tree -n -I __pycache__ --sort=name --noreport --dirsfirst {p}"
    # print(cmd)
    output = check_output(cmd, shell=True)
    output = output.decode()
    output = output.split("\n")[1:]  # eliminate 1st line
    output = "\n".join(output)
    return make_markdown("", output)


def extract_text(p: Path) -> str:
    suffix = p.suffix.split(".")[-1]
    text = p.read_text()
    return make_markdown(suffix, text)


def main(proj_dir: Path) -> None:
    # some basic checks
    if not proj_dir.exists():
        raise Exception(f"{proj_dir} does not exist.")
    elif not proj_dir.is_dir():
        raise Exception(f"{proj_dir} is not a dir.")

    # recursively iterate dir
    code_blocks = {}
    for p in proj_dir.rglob("*"):
        if p.is_file() and not SPEC.match_file(p):
            name = p.relative_to(proj_dir)
            try:
                code_blocks[name] = make_markdown(p)
            except Exception:
                print(f"Can not read: {name}")

    # compile to single file
    tree = make_filetree(proj_dir)
    comp = "\n\n".join((tree, *code_blocks.values()))
    OUTPUT_FILE.write_text(comp)


if __name__ == "__main__":
    proj_dir = Path(sys.argv[1])
    main(proj_dir)
