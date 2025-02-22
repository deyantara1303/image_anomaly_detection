"""Helper script to scan through all images_anom in the source dir and its subdirs and
incrementally rename them as image0000x.
Copy the renamed files in destination dir"""

import os
import shutil

SOURCE_DIR = "input"
DEST_DIR = "output"

def copy_and_rename_dataset(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    image_extensions = (".png", ".jpg")
    image_files = []

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(os.path.join(root, file))

    image_files.sort()

    for index, image_path in enumerate(image_files, start=1):
        ext = os.path.splitext(image_path)[1].lower()
        new_filename = f"image{index:05d}{ext}"
        new_path = os.path.join(destination_dir, new_filename)

        shutil.copy2(image_path, new_path)
        print(f"Copied: {image_path} -> {new_path}")


if __name__ == "__main__":
    copy_and_rename_dataset(SOURCE_DIR, DEST_DIR)