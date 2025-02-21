from anomalib.engine import Engine

DEFAULT_CKPT_PATH = "results/checkpoints/epoch_.ckpt"
DEFAULT_CONFIG_PATH = "configs/experiments/test_data.yaml"

if __name__ == "__main__":
    engine, model, datamodule = Engine.from_config(DEFAULT_CONFIG_PATH)
    engine = Engine(image_metrics={
        "Precision": {
            "class_path": "torchmetrics.Precision",
            "init_args": {"task": "binary"}
        },
        "Recall": {
            "class_path": "torchmetrics.Recall",
            "init_args": {"task": "binary"}
        }
    })
    engine.test(datamodule=datamodule, model=model, ckpt_path=DEFAULT_CKPT_PATH, verbose=True)
