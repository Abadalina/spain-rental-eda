"""
Helper functions for data cleaning and visualisation.
Author: Alejandro Abadal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# ── Project colour palette ───────────────────────────────────────────────────
PALETTE = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
PRIMARY  = "#2a9d8f"
ACCENT   = "#e76f51"

def set_style():
    """Apply global visual style for the project."""
    sns.set_theme(style="whitegrid", palette=PALETTE)
    plt.rcParams.update({
        "figure.facecolor": "#fafafa",
        "axes.facecolor":   "#fafafa",
        "axes.spines.top":  False,
        "axes.spines.right":False,
        "font.family":      "DejaVu Sans",
        "axes.titlesize":   14,
        "axes.titleweight": "bold",
        "axes.labelsize":   11,
    })


# ── Cleaning ──────────────────────────────────────────────────────────────────
def clean_price(series: pd.Series) -> pd.Series:
    """Convert price column from string ($1,200.00) to float."""
    return (
        series.astype(str)
        .str.replace(r"[\$,]", "", regex=True)
        .str.strip()
        .replace("", np.nan)
        .astype(float)
    )


def remove_price_outliers(df: pd.DataFrame, col: str = "price",
                          lower: float = 0.01, upper: float = 0.99) -> pd.DataFrame:
    """Remove price outliers using percentile clipping."""
    q_low  = df[col].quantile(lower)
    q_high = df[col].quantile(upper)
    mask   = df[col].between(q_low, q_high)
    n_removed = (~mask).sum()
    print(f"  Outliers removed: {n_removed} ({n_removed/len(df)*100:.1f}%)")
    return df[mask].copy()


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning pipeline for the Airbnb dataset."""
    print("── Data cleaning ──────────────────────────────")
    print(f"  Initial rows: {len(df):,}")

    # Price — compatible with pandas 3.0 (StringDtype) and older versions (object)
    if not pd.api.types.is_numeric_dtype(df["price"]):
        df["price"] = clean_price(df["price"])

    # Drop rows with no price or coordinates
    before = len(df)
    df = df.dropna(subset=["price", "latitude", "longitude"])
    print(f"  Rows dropped (no price/coords): {before - len(df)}")

    # Remove impossible prices
    df = df[df["price"] > 0]

    # Remove long-stay-only listings (min nights > 365)
    if "minimum_nights" in df.columns:
        df = df[df["minimum_nights"] <= 365]

    # Remove price outliers
    df = remove_price_outliers(df)

    df = df.reset_index(drop=True)
    print(f"  Final rows: {len(df):,}")
    print("───────────────────────────────────────────────\n")
    return df


# ── Visualisation helpers ─────────────────────────────────────────────────────
def save_fig(fig, filename: str, dpi: int = 150):
    """Save figure to outputs/figures/."""
    import os
    os.makedirs("../outputs/figures", exist_ok=True)
    path = f"../outputs/figures/{filename}.png"
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"  Figure saved -> {path}")


def fmt_euro(x, pos=None):
    """Axis formatter to display euros."""
    return f"{x:,.0f} €"


def top_neighbourhoods(df: pd.DataFrame, n: int = 15,
                       col: str = "neighbourhood_cleansed") -> pd.Series:
    """Return the n neighbourhoods with the most listings."""
    return df[col].value_counts().head(n)
