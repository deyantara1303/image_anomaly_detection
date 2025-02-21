from anomalib.engine import Engine

"""Set this config path for custom experiments. 
    Default is set to a dummy experiment"""
CONFIG_PATH = "configs/experiments/experiment_default.yaml"

if __name__ == "__main__":
    """Fetch the engine, model and datamodule from the config, and train the respective model on the given datamodule"""
    engine, model, datamodule = Engine.from_config(CONFIG_PATH)
    engine.train(datamodule=datamodule, model=model)

