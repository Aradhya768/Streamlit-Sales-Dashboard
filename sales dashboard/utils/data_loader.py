import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/superstore.csv",
        encoding="latin1"
    )

    df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed")


    df["Month"] = df["Order Date"].dt.strftime("%b")

    df["Year"] = df["Order Date"].dt.year

    return df