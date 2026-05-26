from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "superstore.csv"

def load_data():

    df = pd.read_csv(DATA_PATH, encoding="latin1")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="mixed"
    )

    df["Month"] = df["Order Date"].dt.strftime("%b")

    df["Year"] = df["Order Date"].dt.year

    return df
