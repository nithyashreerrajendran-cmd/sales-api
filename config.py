"""
config.py — Loads settings from .env
"""
# config.py
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")
KAGGLE_DATASET = os.getenv("KAGGLE_DATASET", "kyanyoga/sample-sales-data")
OUTPUT_FILE = os.getenv("OUTPUT_FILE")
DECIMAL_PLACES = int(os.getenv("DECIMAL_PLACES", 2))