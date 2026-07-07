import os

# Application Configuration
APP_TITLE = "OSINT Tools Comparison & Intelligence Dashboard"
APP_ICON = "🔍"
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DATA_FILE_PATH = os.path.join(DATA_DIR, "osint_tools_dataset.json")

# Scoring Matrix Weights (Must sum to 1.0)
WEIGHTS = {
    "features": 0.15,
    "ease_of_use": 0.10,
    "accuracy": 0.15,
    "performance": 0.15,
    "automation": 0.15,
    "reporting": 0.10,
    "data_sources": 0.20
}