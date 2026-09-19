import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "cavins_sales_cleaned.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "processed"


def load_data():
    """Load cleaned sales data."""

    df = pd.read_csv(INPUT_FILE)

    df["order_date"] = pd.to_datetime(df["order_date"])

    return df


def product_analysis(df):
    """Product-wise demand analysis."""

    result = (
        df.groupby("product", as_index=False)["sold_qty"]
        .sum()
        .sort_values("sold_qty", ascending=False)
    )

    result.to_csv(
        OUTPUT_DIR / "product_performance.csv",
        index=False
    )

    return result


def district_analysis(df):
    """District-wise demand analysis."""

    result = (
        df.groupby("district", as_index=False)["sold_qty"]
        .sum()
        .sort_values("sold_qty", ascending=False)
    )

    result.to_csv(
        OUTPUT_DIR / "district_performance.csv",
        index=False
    )

    return result


def monthly_analysis(df):
    """Monthly demand analysis."""

    result = (
        df.groupby(
            df["order_date"].dt.to_period("M")
        )["sold_qty"]
        .sum()
        .reset_index()
    )

    result["order_date"] = result["order_date"].astype(str)

    result.to_csv(
        OUTPUT_DIR / "monthly_sales.csv",
        index=False
    )

    return result


def yearly_analysis(df):
    """Year-wise demand analysis."""

    result = (
        df.groupby(
            df["order_date"].dt.year
        )["sold_qty"]
        .sum()
        .reset_index()
    )

    result.rename(
        columns={"order_date": "year"},
        inplace=True
    )

    result.to_csv(
        OUTPUT_DIR / "yearly_sales.csv",
        index=False
    )

    return result


def product_district_analysis(df):
    """Product × district demand analysis."""

    result = (
        df.groupby(
            ["product", "district"],
            as_index=False
        )["sold_qty"]
        .sum()
        .sort_values("sold_qty", ascending=False)
    )

    result.to_csv(
        OUTPUT_DIR / "product_district_performance.csv",
        index=False
    )

    return result


def main():

    print("Loading cleaned dataset...")

    df = load_data()

    print(f"Rows: {len(df):,}")

    print("\nGenerating business analysis...")

    product = product_analysis(df)
    district = district_analysis(df)
    monthly = monthly_analysis(df)
    yearly = yearly_analysis(df)
    product_district = product_district_analysis(df)

    print("\nTop 5 products:")
    print(product.head().to_string(index=False))

    print("\nTop 5 districts:")
    print(district.head().to_string(index=False))

    print("\nYearly demand:")
    print(yearly.to_string(index=False))

    print("\nAnalysis files generated successfully.")


if __name__ == "__main__":
    main()