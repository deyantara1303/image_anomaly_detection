"""Helper script to scan through all images_anom in the source dir and its subdirs
and copy the files in destination dir"""

import os
import shutil

SOURCE_DIR = "input"
DEST_DIR = "output"

def copy_dataset(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    image_extensions = (".png", ".jpg")

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(destination_dir, file)

                #shutil.copy2(source_file, dest_file)
                shutil.move(source_file, dest_file)
                print(f"Copied or moved: {source_file} -> {dest_file}")

if __name__ == "__main__":
    copy_dataset(SOURCE_DIR, DEST_DIR)