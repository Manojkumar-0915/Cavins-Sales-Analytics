import pandas as pd
import numpy as np
from pathlib import Path

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "cavins_sales_cleaned.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "processed"


def load_monthly_data():
    """Load cleaned data and aggregate demand by month."""

    df = pd.read_csv(INPUT_FILE)

    df["order_date"] = pd.to_datetime(df["order_date"])

    monthly = (
        df.groupby(
            df["order_date"].dt.to_period("M")
        )["sold_qty"]
        .sum()
        .sort_index()
    )

    return monthly


def seasonal_naive_forecast(train, test):
    """Forecast using the same month from the previous year."""

    predictions = []

    for period in test.index:
        previous_year = period - 12

        if previous_year in train.index:
            predictions.append(train.loc[previous_year])
        else:
            predictions.append(np.nan)

    return pd.Series(
        predictions,
        index=test.index
    )


def evaluate(actual, predicted):
    """Calculate forecasting metrics."""

    valid = predicted.notna()

    actual = actual[valid]
    predicted = predicted[valid]

    mae = mean_absolute_error(
        actual,
        predicted
    )

    rmse = np.sqrt(
        mean_squared_error(
            actual,
            predicted
        )
    )

    mape = (
        np.mean(
            np.abs(
                (actual - predicted) / actual
            )
        )
        * 100
    )

    return mae, rmse, mape


def main():

    print("Loading monthly demand data...")

    monthly = load_monthly_data()

    # Same test period used during model comparison
    train = monthly[
        monthly.index < "2025-01"
    ]

    test = monthly[
        monthly.index >= "2025-01"
    ]

    print(f"Training months: {len(train)}")
    print(f"Testing months: {len(test)}")

    # --------------------------------------------------
    # Seasonal Naive Baseline
    # --------------------------------------------------

    baseline_pred = seasonal_naive_forecast(
        train,
        test
    )

    baseline_mae, baseline_rmse, baseline_mape = evaluate(
        test,
        baseline_pred
    )

    # --------------------------------------------------
    # Holt-Winters
    # --------------------------------------------------

    model = ExponentialSmoothing(
        train,
        trend="add",
        seasonal="add",
        seasonal_periods=12
    ).fit(
        optimized=True
    )

    hw_pred = model.forecast(
        len(test)
    )

    hw_pred.index = test.index

    hw_mae, hw_rmse, hw_mape = evaluate(
        test,
        hw_pred
    )

    # --------------------------------------------------
    # Forecast comparison
    # --------------------------------------------------

    comparison = pd.DataFrame({
        "month": test.index.astype(str),
        "actual": test.values,
        "seasonal_naive": baseline_pred.values,
        "holt_winters": hw_pred.values
    })

    comparison.to_csv(
        OUTPUT_DIR / "forecast_comparison.csv",
        index=False
    )

    # --------------------------------------------------
    # Model metrics
    # --------------------------------------------------

    metrics = pd.DataFrame({
        "model": [
            "Seasonal Naive",
            "Holt-Winters"
        ],
        "MAE": [
            baseline_mae,
            hw_mae
        ],
        "RMSE": [
            baseline_rmse,
            hw_rmse
        ],
        "MAPE": [
            baseline_mape,
            hw_mape
        ]
    })

    metrics.to_csv(
        OUTPUT_DIR / "forecast_metrics.csv",
        index=False
    )

    # --------------------------------------------------
    # Display results
    # --------------------------------------------------

    print("\nForecast comparison:")
    print(
        comparison.to_string(index=False)
    )

    print("\nModel evaluation:")
    print(
        metrics.round(2).to_string(index=False)
    )

    print("\nForecasting files generated successfully.")


if __name__ == "__main__":
    main()