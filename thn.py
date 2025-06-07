from datetime import datetime
from pathlib import Path
from PIL import Image
import argparse
import os
import sys

PROG = 'thn'

def main():
    parser = argparse.ArgumentParser(prog = PROG, add_help = False)
    parser.add_argument('-s', '--src-dir', required = True)
    parser.add_argument('-d', '--dst-dir', required = True)
    parser.add_argument('-f', '--format', choices=['jpg', 'png'], required = True)
    parser.add_argument('-h', '--height', type = int, required = True)
    parser.add_argument('-i', '--interval', type = int, required = True)
    args = parser.parse_args()

    print("Starting thumbnail generation with the following arguments:")
    print(f"Source directory: {args.src_dir}")
    print(f"Destination directory: {args.dst_dir}")
    print(f"Format: {args.format}")
    print(f"Height: {args.height}")
    print(f"Interval: {args.interval}")

    require_dir_exists(args.src_dir, 'source directory')
    require_dir_exists(args.dst_dir, 'destination directory')
    require_positive_int(args.height, 'height')
    require_positive_int(args.interval, 'interval')

    files = collect_files(args.src_dir, args.interval)
    if len(files) == 0:
        print(f"None of the files in {args.src_dir} fit the specified criteria.")
        sys.exit(1)
    print("Considering the following files:")
    for file in files:
        print(file)
    for file in files:
        print(f"Creating thumbnail for {file}...")
        create_thumbnail(file, args.dst_dir, args.format, args.height)
        print("Done!")
    print("All done!")

def require_dir_exists(path, arg_name):
    if not os.path.isdir(path):
        print(f"Error: the provided {arg_name} does not exist: {path}")
        sys.exit(1)

def require_positive_int(x, arg_name):
    if x <= 0:
        print(f"Error: the provided {arg_name} is not a positive integer: {x}")
        sys.exit(1)

def collect_files(src_dir, interval_hours):
    folder = Path(src_dir)
    cutoff = datetime.now().timestamp() - interval_hours * 3600  # cutoff time in seconds
    return [
        f for f in folder.iterdir()
        if (
            f.is_file() and
            f.suffix.lower() in {'.jpg', '.png'} and
            f.stat().st_mtime >= cutoff
        )
    ]

def create_thumbnail(file, dst_dir, format, height):
    with Image.open(file) as img:
        orig_width, orig_height = img.size
        aspect_ratio = orig_width / orig_height
        width = int(height * aspect_ratio)
        resized_img = img.resize((width, height))
        output_file_name = f"{file.stem}_thumbnail.{format}"
        output_path = f"{dst_dir}{os.path.sep}{output_file_name}"
        resized_img.save(output_path)

if __name__ == "__main__":
    main()
