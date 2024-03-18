from pathlib import Path
import forecaster

PACKAGE_ROOT = Path(forecaster.__file__).resolve().parent
DATASET_DIR = PACKAGE_ROOT / "datasets"