import argparse
from pathlib import Path
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Sort files")
    parser.add_argument(
        "-S", "--source", type=Path, help="Path to the source directory."
    )
    parser.add_argument(
        "-D",
        "--destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Path to the destination directory.",
    )
    return parser.parse_args()


def sort_files(path: Path, dist: Path):
    if path.exists():
        try:
            for obj in path.iterdir():
                if obj.is_dir():
                    sort_files(obj, dist)
                else:
                    ext = obj.suffix[1:] if obj.suffix else "files_without_extension"
                    new_path = dist / ext
                    new_path.mkdir(exist_ok=True, parents=True)
                    try:
                        shutil.copyfile(obj, new_path / obj.name)
                    except Exception as e:
                        print(f"Cannot copy file {obj}: {e}")
        except Exception as e:
            print(f"No access to directory {obj}: {e}")
    else:
        print("This directory doesn't exist")


if __name__ == "__main__":
    args = parse_args()
    sort_files(args.source, args.destination)