"""
writer.py — Writes results back to CSV
"""
import os
import sys
import pandas as pd


def write_csv(df: pd.DataFrame, output_path: str, label: str = "Results") -> None:
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"💾 {label} saved to '{output_path}' — {len(df)} rows")

    except PermissionError:
        print(f"❌ Permission denied: '{output_path}'")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error writing file: {e}")
        sys.exit(1)


def write_all(results: dict, base_path: str) -> None:
    """Write multiple DataFrames — one CSV per result."""
    folder = os.path.dirname(base_path)
    for name, df in results.items():
        path = os.path.join(folder, f"{name}.csv")
        write_csv(df, path, label=name)