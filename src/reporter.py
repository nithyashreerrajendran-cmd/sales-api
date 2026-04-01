"""
reporter.py — Prints summary tables to the console
"""
import pandas as pd


def print_report(
    by_country: pd.DataFrame,
    by_product: pd.DataFrame,
    by_year: pd.DataFrame,
    by_deal: pd.DataFrame,
    top_cust: pd.DataFrame,
) -> None:

    print("\n" + "═" * 55)
    print("            SALES DATA REPORT")
    print("═" * 55)

    print("\n📦 Sales by Product Line:")
    print(by_product.to_string(index=False))

    print("\n🌍 Sales by Country (Top 10):")
    print(by_country.head(10).to_string(index=False))

    print("\n📅 Sales by Year:")
    print(by_year.to_string(index=False))

    print("\n💼 Sales by Deal Size:")
    print(by_deal.to_string(index=False))

    print("\n🏆 Top 10 Customers:")
    print(top_cust.to_string(index=False))

    print("\n" + "═" * 55 + "\n")