from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"

BBOX = {
    "min_lat": -11.0,
    "max_lat": 6.0,
    "min_lon": 95.0,
    "max_lon": 141.0,
}

CATALOG_START = "1990-01-01"   
CATALOG_MIN_MAG = 4.0          
USGS_API = "https://earthquake.usgs.gov/fdsnws/event/1/query"

FORECAST_MIN_MAG = 4.5
GRID_DEG = 1.0
FORECAST_FREQ = "MS"

TRAIN_END = "2018-12-31"
VALID_END = "2021-12-31"

RANDOM_SEED = 42