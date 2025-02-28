"""Helper script to move files ending with a token"""

import os
import shutil

def move_files_with_end_token(source_dir, dest_dir, ending_token):
    """Move files with ending token to dest_dir."""
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return

    os.makedirs(dest_dir, exist_ok=True)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(ending_token):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                counter = 1
                base, ext = os.path.splitext(file)
                while os.path.exists(dest_file):
                    dest_file = os.path.join(dest_dir, base + f"_{counter}{ext}")
                    counter += 1
                try:
                    shutil.move(source_file, dest_file)
                    print(f"Moving {source_file} to {dest_file}")
                except Exception as e:
                    print(f"Failed to move {source_file} to {dest_file}: {e}")

if __name__ == "__main__":
    source_dir = "input"
    dest_dir = "output"
    ending_token = "xxx"
    move_files_with_end_token(source_dir, dest_dir, ending_token)