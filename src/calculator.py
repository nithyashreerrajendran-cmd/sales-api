"""
calculator.py — All sales calculations
"""
import sys
import pandas as pd


def sales_by_country(df: pd.DataFrame, dp: int) -> pd.DataFrame:
    """Total and average sales grouped by country."""
    try:
        result = (
            df.groupby("COUNTRY")["SALES"]
            .agg(total_sales="sum", avg_sales="mean", order_count="count")
            .round(dp)
            .reset_index()
            .sort_values("total_sales", ascending=False)
        )
        return result
    except Exception as e:
        print(f"❌ Error in sales_by_country: {e}")
        sys.exit(1)


def sales_by_productline(df: pd.DataFrame, dp: int) -> pd.DataFrame:
    """Total sales and quantity ordered per product line."""
    try:
        result = (
            df.groupby("PRODUCTLINE")
            .agg(
                total_sales=("SALES", "sum"),
                total_qty=("QUANTITYORDERED", "sum"),
                avg_price=("PRICEEACH", "mean"),
            )
            .round(dp)
            .reset_index()
            .sort_values("total_sales", ascending=False)
        )
        return result
    except Exception as e:
        print(f"❌ Error in sales_by_productline: {e}")
        sys.exit(1)


def sales_by_year(df: pd.DataFrame, dp: int) -> pd.DataFrame:
    """Total sales broken down by year."""
    try:
        result = (
            df.groupby("YEAR_ID")["SALES"]
            .agg(total_sales="sum", order_count="count")
            .round(dp)
            .reset_index()
        )
        return result
    except Exception as e:
        print(f"❌ Error in sales_by_year: {e}")
        sys.exit(1)


def sales_by_dealsize(df: pd.DataFrame, dp: int) -> pd.DataFrame:
    """Count and total sales per deal size (Small / Medium / Large)."""
    try:
        result = (
            df.groupby("DEALSIZE")["SALES"]
            .agg(total_sales="sum", deal_count="count")
            .round(dp)
            .reset_index()
            .sort_values("total_sales", ascending=False)
        )
        return result
    except Exception as e:
        print(f"❌ Error in sales_by_dealsize: {e}")
        sys.exit(1)


def top_customers(df: pd.DataFrame, dp: int, top_n: int = 10) -> pd.DataFrame:
    """Top N customers by total sales."""
    try:
        result = (
            df.groupby("CUSTOMERNAME")["SALES"]
            .sum()
            .round(dp)
            .reset_index()
            .rename(columns={"SALES": "total_sales"})
            .sort_values("total_sales", ascending=False)
            .head(top_n)
        )
        return result
    except Exception as e:
        print(f"❌ Error in top_customers: {e}")
        sys.exit(1)