"""Helper script to split dataset into training and test set"""

import splitfolders

SOURCE_DIR = "input"
DEST_DIR = "output"
TEST_RATIO = 0.6
SEED = 42

def split_dataset(source_dir, destination_dir, test_ratio=0.3, seed=42):
    """Splits dataset into training and test sets while preserving class structure

    Args:
        source_dir (str): Path to dataset containing class-wise data
        destination_dir (str): Path where train/test folders will be stored.
        test_ratio (float): Ratio of test data
        seed (int): Random seed for reproducibility
    """

    splitfolders.ratio(
        source_dir,
        destination_dir,
        seed,
        ratio=(1-test_ratio, test_ratio),
        group_prefix=None,
        move=False
    )

if __name__ == "__main__":
    split_dataset(SOURCE_DIR, DEST_DIR, TEST_RATIO, SEED)
