import os
import shutil
import argparse

def recursive_copy(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(dest_dir, item)

            if os.path.isdir(src_path):
                recursive_copy(src_path, dest_path)
            else:
                copy_file_to_sorted_dir(src_path, dest_dir)

    except Exception as e:
        print(f"Error: {e}")

def copy_file_to_sorted_dir(src_file, dest_dir):
    try:
        extension = os.path.splitext(src_file)[1][1:]  
        dest_subdir = os.path.join(dest_dir, extension)

        os.makedirs(dest_subdir, exist_ok=True)
        shutil.copy2(src_file, dest_subdir)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursive file copy and sorting")
    parser.add_argument("src_dir", help="Source directory path")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory path (default: 'dist')")
    args = parser.parse_args()

    src_dir = os.path.abspath(args.src_dir)
    dest_dir = os.path.abspath(args.dest_dir)

    recursive_copy(src_dir, dest_dir)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()