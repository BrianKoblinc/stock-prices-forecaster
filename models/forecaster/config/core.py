from pathlib import Path
import forecaster

PACKAGE_ROOT = Path(forecaster.__file__).resolve().parent
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
FITTED_SCALERS_DIR = PACKAGE_ROOT / "fitted_scalers"

ticker_list = ["AAPL", "GOOG", "MSFT", "AMZN"]
