# =========================================================
# EXECUTIVE OVERVIEW DASHBOARD — SUPERSTORE DATASET
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Executive Dashboard",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("data/superstore.csv", encoding="latin1")

# =========================================================
# DATA CLEANING
# =========================================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed"
)

df["Month"] = df["Order Date"].dt.strftime("%b")

month_order = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

body {
    background-color: #071021;
}

/* MAIN BACKGROUND */
.stApp {
    background-color: #071021;
}

/* KPI CARDS */
.kpi-card {
    background: linear-gradient(145deg, #0f172a, #111827);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 4px 25px rgba(0,0,0,0.35);
    transition: 0.3s ease-in-out;
}

.kpi-card:hover {
    transform: translateY(-4px);
}

.kpi-title {
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 10px;
}

.kpi-value {
    color: white;
    font-size: 36px;
    font-weight: 700;
}

.kpi-growth {
    color: #22c55e;
    margin-top: 8px;
    font-size: 14px;
}

/* SECTION TITLES */
.section-title {
    color: white;
    font-size: 26px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* INSIGHT BOX */
.insight-box {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.35);
    padding: 22px;
    border-radius: 18px;
    color: #4ade80;
    line-height: 1.8;
    font-size: 15px;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

left_header, right_header = st.columns([6,1])

with left_header:
    st.title("Executive Overview")

with right_header:
    selected_region = st.selectbox(
        "Region",
        ["All"] + list(df["Region"].unique())
    )

# =========================================================
# FILTER DATA
# =========================================================

if selected_region != "All":
    filtered_df = df[df["Region"] == selected_region]
else:
    filtered_df = df.copy()

# =========================================================
# KPI CALCULATIONS
# =========================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

profit_margin = (total_profit / total_sales) * 100

# =========================================================
# KPI SECTION
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Sales</div>
        <div class="kpi-value">${total_sales:,.0f}</div>
        <div class="kpi-growth">↑ Strong revenue growth</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Profit</div>
        <div class="kpi-value">${total_profit:,.0f}</div>
        <div class="kpi-growth">↑ Profit improving</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Orders</div>
        <div class="kpi-value">{total_orders}</div>
        <div class="kpi-growth">↑ Order volume rising</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Profit Margin</div>
        <div class="kpi-value">{profit_margin:.2f}%</div>
        <div class="kpi-growth">↑ Healthy business margin</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# BUSINESS PERFORMANCE TITLE
# =========================================================

st.markdown(
    '<div class="section-title">Business Performance</div>',
    unsafe_allow_html=True
)

# =========================================================
# MONTHLY SALES TREND
# =========================================================

monthly_sales = (
    filtered_df
    .groupby("Month")["Sales"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

# =========================================================
# CATEGORY PROFIT
# =========================================================

category_profit = (
    filtered_df
    .groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

# =========================================================
# CHART LAYOUT
# =========================================================

left_chart, right_chart = st.columns([2,1])

# =========================================================
# LINE CHART
# =========================================================

with left_chart:

    line_fig = px.line(
        monthly_sales,
        x="Month",
        y="Sales",
        markers=True,
        template="plotly_dark"
    )

    line_fig.update_layout(
        paper_bgcolor="#0b1220",
        plot_bgcolor="#0b1220",
        font_color="white",
        height=420,
        title="Monthly Sales Trend"
    )

    st.plotly_chart(
        line_fig,
        use_container_width=True
    )

# =========================================================
# DONUT CHART
# =========================================================

with right_chart:

    donut_fig = px.pie(
        category_profit,
        names="Category",
        values="Profit",
        hole=0.65,
        template="plotly_dark"
    )

    donut_fig.update_layout(
        paper_bgcolor="#0b1220",
        font_color="white",
        height=420,
        title="Profit by Category"
    )

    st.plotly_chart(
        donut_fig,
        use_container_width=True
    )

# =========================================================
# REGIONAL INSIGHTS SECTION
# =========================================================

st.markdown(
    '<div class="section-title">Regional Insights</div>',
    unsafe_allow_html=True
)

# =========================================================
# REGION SALES
# =========================================================

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

bottom_left, bottom_right = st.columns([1.5,1])

# =========================================================
# BAR CHART
# =========================================================

with bottom_left:

    bar_fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        template="plotly_dark",
        text_auto=True
    )

    bar_fig.update_layout(
        paper_bgcolor="#0b1220",
        plot_bgcolor="#0b1220",
        font_color="white",
        height=380,
        title="Sales by Region"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

# =========================================================
# INSIGHTS BOX
# =========================================================

with bottom_right:

    top_region = (
        region_sales
        .sort_values(by="Sales", ascending=False)
        .iloc[0]["Region"]
    )

    top_category = (
        category_profit
        .sort_values(by="Profit", ascending=False)
        .iloc[0]["Category"]
    )

    st.markdown(f"""
    <div class="insight-box">

    <h3 style="color:white;">
    Executive Insights
    </h3>

    • <b>{top_region}</b> region generated the highest sales.<br>

    • <b>{top_category}</b> category contributed the highest profit.<br>

    • Business margins remain stable and healthy.<br>

    • Sales trend indicates strong customer demand.<br>

    • Overall performance is steadily improving.

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TOP PRODUCTS SECTION
# =========================================================

st.markdown(
    '<div class="section-title">Top Performing Products</div>',
    unsafe_allow_html=True
)

# =========================================================
# TOP PRODUCTS TABLE
# =========================================================

top_products = (
    filtered_df
    .groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

top_products.columns = ["Product Name", "Revenue"]

top_products["Revenue"] = top_products["Revenue"].apply(
    lambda x: f"${x:,.0f}"
)

st.dataframe(
    top_products,
    use_container_width=True,
    hide_index=True
)
