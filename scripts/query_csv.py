import os
import shutil
import pandas as pd

def move_images_from_csv (csv_path, source_dir, dest_dir, pred_val, pred_key="Pred_Labels", image_path="Image Path"):
    """Moves images on a specified prediction label to the destination folder"""

    df = pd.read_csv(csv_path)
    sel_rows = df[df[pred_key] == pred_val]

    move_count = 0
    os.makedirs(dest_dir, exist_ok=True)
    image_paths = sel_rows[image_path].apply(lambda x: os.path.basename(str(x).strip().strip("[]'\""))).tolist()
    for path in image_paths:
        full_img_path = os.path.join(source_dir, path)
        print(f"Processed filename: {repr(full_img_path)}")
        if os.path.exists(full_img_path):
            shutil.move(full_img_path, os.path.join(dest_dir, os.path.basename(path)))
            move_count += 1
        else:
            print(f"Warning: Image not found - {full_img_path}")

    print(f"Moved {move_count} images with {pred_val} to {dest_dir}")


if __name__ == "__main__":
    # Move False negatives from anomaly inference results
    csv_path = "inference_result.csv"
    source_dir = "../results/images"
    dest_folder_fn = "../results/fn"
    move_images_from_csv(csv_path, source_dir, dest_folder_fn, "tensor([False])")

    # Move False positives from normal inference results
    csv_path = "inference_result.csv"
    source_dir = "../results/images"
    dest_folder_fn = "../results/fp"
    move_images_from_csv(csv_path, source_dir, dest_folder_fn, "tensor([True])")
