# Import required modules
import os
from pathlib import Path
import argparse
from anomalib.data import PredictDataset
from anomalib.engine import Engine
from anomalib.models import EfficientAd
import pandas as pd
from datetime import datetime

DEFAULT_CKPT_PATH = "results/EfficientAd/checkpoints/epoch_.ckpt"

def run_inference(ckpt_path=DEFAULT_CKPT_PATH):
    # Initialize the model and load weights
    model = EfficientAd()
    engine = Engine()
    # Prepare test data
    # You can use a single image or a directory of images
    dataset = PredictDataset(
        path=Path("datasets/"),
        image_size=(256, 256),
    )
    # 4. Get predictions
    pred = engine.predict(
        model=model,
        dataset=dataset,
        ckpt_path=DEFAULT_CKPT_PATH,
    )

    return pred

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Anomalib Inference Parser")
    parser.add_argument("config_path", nargs="?", default=DEFAULT_CKPT_PATH, help="Path to the model checkpoint file")
    args = parser.parse_args()

    # Run inference predictions
    predictions = run_inference()
    image_paths = []
    pred_labels = []
    pred_scores = []
    if predictions is not None:
        for prediction in predictions:
            image_paths.append(prediction['image_path'])
            #anomaly_map = prediction['anomaly_map']  # Pixel-level anomaly heatmap
            pred_labels.append(prediction['pred_labels'])  # Image-level label (0: normal, 1: anomalous)
            pred_scores.append(prediction['pred_scores'])  # Image-level anomaly score

    # Store inference results in a dataframe
    results_df = pd.DataFrame({
        'Image Path': image_paths,
        'Pred_Labels': pred_labels,
        'Pred_Scores': pred_scores
    })

    # Export to csv file in reports/ dir based on time stamp.
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    reports_dir = f'reports/report_{current_time}'
    os.makedirs(reports_dir, exist_ok=True)
    csv_path = os.path.join(reports_dir, 'inference_result.csv')
    results_df.to_csv(csv_path, index=False)
