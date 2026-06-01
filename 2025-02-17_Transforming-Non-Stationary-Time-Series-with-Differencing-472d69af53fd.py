# Description: Short example for Transforming Non Stationary Time Series with Differencing.

# Load the dataset

import matplotlib.pyplot as plt
import pandas as pd
from data_io import read_csv


def main():
    url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    # Read the dataset and skip the first row to ensure correct formatting
    df = read_csv(url, skiprows=1)
    # Rename columns for convenience
    df.rename(columns={"Year": "Year", "J-D": "Temperature Anomaly"}, inplace=True)
    # Convert temperature anomaly column to numeric, forcing errors to NaN
    df["Temperature Anomaly"] = pd.to_numeric(df["Temperature Anomaly"], errors="coerce")
    # Drop rows with missing values
    df.dropna(inplace=True)
    # Ensure the Year column is also numeric
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    # First differencing
    df["First Difference"] = df["Temperature Anomaly"].diff()
    # Second differencing
    df["Second Difference"] = df["First Difference"].diff()
    # Create figure and subplots
    fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    # Original time series
    axes[0].plot(df["Year"], df["Temperature Anomaly"], color="black")
    axes[0].set_title("Global Surface Temperature Anomalies (1880-2020)", fontsize=12)
    axes[0].set_ylabel("Temperature Anomaly (°C)", fontsize=10)
    # First differencing plot
    axes[1].plot(df["Year"], df["First Difference"], color="black")
    axes[1].set_title("First Difference of Global Temperature Anomalies", fontsize=12)
    axes[1].set_ylabel("First Difference (°C)", fontsize=10)
    # Second differencing plot
    axes[2].plot(df["Year"], df["Second Difference"], color="black")
    axes[2].set_title("Second Difference of Global Temperature Anomalies", fontsize=12)
    axes[2].set_xlabel("Year", fontsize=10)
    axes[2].set_ylabel("Second Difference (°C)", fontsize=10)
    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
    plt.savefig("global_temp_anomalies_analysis.png")
    plt.show()


if __name__ == "__main__":
    main()
