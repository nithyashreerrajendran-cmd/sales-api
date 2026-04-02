"""
main.py — Entry point. Runs the full sales analysis pipeline.

Usage:
    python main.py
"""
import os
import sys
import kaggle
import config
from src.loader     import load_sales
from src.calculator import (
    sales_by_country,
    sales_by_productline,
    sales_by_year,
    sales_by_dealsize,
    top_customers,
)
from src.reporter import print_report
from src.writer   import write_all


def main() -> None:
    print("\n Starting Sales Analyser...\n")

    # 1. Load
    os.environ["KAGGLE_USERNAME"] = config.KAGGLE_USERNAME
    os.environ["KAGGLE_KEY"]      = config.KAGGLE_KEY

    if not os.path.exists("data/raw/sales_data_sample.csv"):
        print("Downloading dataset from Kaggle...")
        os.makedirs("data/raw", exist_ok=True)
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            config.KAGGLE_DATASET,
            path="data/raw",
            unzip=True
        )
        print("Download complete.")
    else:
        print("Using existing local file.")
    df = load_sales()
    dp = config.DECIMAL_PLACES

    # 2. Calculate
    by_country = sales_by_country(df, dp)
    by_product = sales_by_productline(df, dp)
    by_year    = sales_by_year(df, dp)
    by_deal    = sales_by_dealsize(df, dp)
    top_cust   = top_customers(df, dp)

    # 3. Report
    print_report(by_country, by_product, by_year, by_deal, top_cust)

    # 4. Write all results
    write_all(
        {
            "sales_by_country":     by_country,
            "sales_by_productline": by_product,
            "sales_by_year":        by_year,
            "sales_by_dealsize":    by_deal,
            "top_customers":        top_cust,
        },
        config.OUTPUT_FILE,
    )

    print("✅ Done.\n")
    sys.exit(0)


if __name__ == "__main__":
    main()