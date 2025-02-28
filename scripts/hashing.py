"""Helper script to compare two directories and move common files
Useful to check if train and test set are mutually exclusive."""

import os
import hashlib
import shutil

def calculate_file_hash(file_path, hash_func=hashlib.sha256):
    hasher = hash_func()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    return hasher.hexdigest()

def get_file_hashes(folder):
    file_hashes = {}
    if not os.path.exists(folder):
        print(f"Folder {folder} doesn't exist")
        return
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash:
                file_hashes[file_hash] = file_path
    return file_hashes

def compare_and_move(dir1, dir2, outdir):
    hashes_folder1 = get_file_hashes(dir1)
    hashes_folder2 = get_file_hashes(dir2)

    common_files = hashes_folder1.keys() & hashes_folder2.keys()
    if not common_files:
        print("No common files")
        return
    for file_hash in common_files:
        os.makedirs(outdir, exist_ok=True)
        file_path = hashes_folder1[file_hash]
        file_name = os.path.basename(file_path)
        output_path = os.path.join(outdir, file_name)

        try:
            shutil.move(file_path, output_path)
            print(f"Moving {file_path} to {output_path}")
        except Exception as e:
            print(f"Error moving {file_path}: {e}")

if __name__ == "__main__":
    dir1 = "../datasets/CowFleisch/sample_XX/test/good"
    dir2 = "../datasets/CowFleisch/sample_XX/train/good"
    outdir = "../datasets/CowFleisch/sample_XX/compare"
    compare_and_move(dir1, dir2, outdir)