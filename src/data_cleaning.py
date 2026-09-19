import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "Cavins_Complete_Districtwise_Sales.xlsx"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

OUTPUT_FILE = PROCESSED_DIR / "cavins_sales_cleaned.csv"


def load_data():
    """Load the main sales sheet from Excel."""
    df = pd.read_excel(RAW_FILE, sheet_name="Data")
    return df


def clean_data(df):
    """Clean and validate the sales dataset."""

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert date column
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Remove completely duplicated rows
    df = df.drop_duplicates()

    # Remove rows with missing critical values
    df = df.dropna(
        subset=[
            "product",
            "district",
            "order_date",
            "sold_qty"
        ]
    )

    # Ensure quantity is numeric
    df["sold_qty"] = pd.to_numeric(
        df["sold_qty"],
        errors="coerce"
    )

    # Remove invalid quantities
    df = df[df["sold_qty"] > 0]

    # Sort chronologically
    df = df.sort_values(
        ["order_date", "product", "district"]
    ).reset_index(drop=True)

    return df


def save_data(df):
    """Save cleaned data to CSV."""

    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )


def main():

    print("Loading dataset...")

    df = load_data()

    print(f"Original rows: {len(df):,}")

    df = clean_data(df)

    print(f"Cleaned rows: {len(df):,}")

    print(f"Date range: {df['order_date'].min().date()} "
          f"to {df['order_date'].max().date()}")

    print(f"Products: {df['product'].nunique()}")

    print(f"Districts: {df['district'].nunique()}")

    save_data(df)

    print("\nCleaned dataset saved successfully.")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()