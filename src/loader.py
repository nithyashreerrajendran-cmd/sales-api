"""
loader.py - Fetches sales CSV from Kaggle
"""
import sys
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def load_sales() -> pd.DataFrame:
    try:
        # Use existing file if already downloaded
        filepath = "data/raw/sales_data_sample.csv"
        
        if not os.path.exists(filepath):
            from kaggle.api.kaggle_api_extended import KaggleApi
            
            os.makedirs("data/raw", exist_ok=True)
            os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME", "")
            os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY", "")

            api = KaggleApi()
            api.authenticate()
            print("Kaggle login successful!")

            # Download as zip then unzip manually
            api.dataset_download_files(
                "kyanyoga/sample-sales-data",
                path="data/raw",
                unzip=False
            )
            print("Downloaded zip!")

            # Unzip manually
            import zipfile
            zip_path = "data/raw/sample-sales-data.zip"
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall("data/raw")
            print("Unzipped!")

        # Read CSV
        df = pd.read_csv(filepath, encoding="latin1")
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
        print(f"Loaded {len(df)} rows!")
        return df

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)