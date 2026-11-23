"""Smoke test Fase 0: memastikan environment dan konfigurasi sehat."""
import importlib

import pytest

from src import config

PACKAGES = ["pandas", "numpy", "scipy", "statsmodels", "sklearn",
            "lightgbm", "plotly", "streamlit", "pyarrow", "requests"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_package_importable(pkg):
    importlib.import_module(pkg)


def test_sklearn_has_hdbscan():
    from sklearn.cluster import HDBSCAN


def test_bbox_valid():
    b = config.BBOX
    assert b["min_lat"] < b["max_lat"]
    assert b["min_lon"] < b["max_lon"]
    assert -90 <= b["min_lat"] and b["max_lat"] <= 90
    assert -180 <= b["min_lon"] and b["max_lon"] <= 180


def test_time_split_ordered():
    assert config.CATALOG_START < config.TRAIN_END < config.VALID_END


def test_forecast_threshold_above_download_threshold():
    assert config.FORECAST_MIN_MAG >= config.CATALOG_MIN_MAG


def test_paths_exist():
    assert config.DATA_RAW.exists()
    assert config.DATA_PROCESSED.exists()