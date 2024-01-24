import shutil
import argparse
from pathlib import Path

def recursive_copy(src_path, dest_dir):
    try:
        src_path = Path(src_path)
        dest_dir = Path(dest_dir)
        dest_dir.mkdir(parents=True, exist_ok=True)

        for item in src_path.iterdir():
            if item.is_dir():
                recursive_copy(item, dest_dir)
            elif item.is_file():
                copy_file_to_sorted_dir(item, dest_dir)

    except Exception as e:
        print(f"Error: {e}")

def copy_file_to_sorted_dir(src_file, dest_dir):
    try:
        extension = src_file.suffix[1:]  # Get file extension without dot
        dest_subdir = dest_dir / extension

        dest_subdir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_subdir / src_file.name
        shutil.copy2(src_file, dest_file)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursive file copy and sorting")
    parser.add_argument("src_path", help="Source path")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory path (default: 'dist')")
    args = parser.parse_args()

    src_path = args.src_path
    dest_dir = args.dest_dir

    recursive_copy(src_path, dest_dir)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()
