from pathlib import Path

PACKAGE_ROOT = Path("/Users/bkoblinc/Desktop/Otros proyectos/stock-prices/stock-prices-forecaster/models/forecaster")
DATASET_DIR = PACKAGE_ROOT.joinpath("datasets")
TRAINED_MODEL_DIR = PACKAGE_ROOT.joinpath("trained_models")
FITTED_SCALERS_DIR = PACKAGE_ROOT.joinpath("fitted_scalers")

ticker_list = ["AAPL", "GOOG", "MSFT", "AMZN"]
