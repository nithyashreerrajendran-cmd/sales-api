"""
loader.py - Fetches sales CSV from Kaggle
"""
import sys
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def load_sales() -> pd.DataFrame:
    try:
        # Login to Kaggle using your .env credentials
        api = KaggleApi()
        api.authenticate()
        print(" Kaggle login successful!")

        # Download CSV from Kaggle into data/raw folder
        api.dataset_download_files(
            "kyanyoga/sample-sales-data",
            path="data/raw",
            unzip=True
        )
        print("Downloaded from Kaggle!")

        # Read the CSV
        df = pd.read_csv("data/raw/sales_data_sample.csv", encoding="latin1")
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
        print(f" Loaded {len(df)} rows, {len(df.columns)} columns")
        return df

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)