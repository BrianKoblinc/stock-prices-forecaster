from typing import Generator

import pandas as pd
import pytest
from app.main import app
from fastapi.testclient import TestClient

from models.forecaster.config.core import config
from models.forecaster.processing.data_manager import load_dataset


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return load_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
