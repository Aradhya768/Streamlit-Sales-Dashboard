import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Sales Analytics",
    layout="wide"
)

# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

/* =========================================
BACKGROUND
========================================= */

.stApp {
    background: transparent;
    color: white;
}

/* AURORA BACKGROUND */

.stApp::before {
    content: "";
    position: fixed;

    top: -50%;
    left: -50%;

    width: 200%;
    height: 200%;

    background:
        radial-gradient(circle at 20% 20%, rgba(56,189,248,0.35), transparent 22%),
        radial-gradient(circle at 80% 30%, rgba(168,85,247,0.32), transparent 22%),
        radial-gradient(circle at 50% 80%, rgba(59,130,246,0.28), transparent 22%),
        radial-gradient(circle at 70% 70%, rgba(34,211,238,0.22), transparent 20%),
        radial-gradient(circle at 40% 50%, rgba(14,165,233,0.18), transparent 18%),
        #020617;

    filter: blur(40px);

    animation: auroraMove 18s ease-in-out infinite alternate;

    z-index: -2;
}

@keyframes auroraMove {

    0% {
        transform: rotate(0deg) scale(1);
    }

    50% {
        transform: rotate(180deg) scale(1.15);
    }

    100% {
        transform: rotate(360deg) scale(1);
    }
}

/* STARS */

.stApp::after {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;

    background-image:
        radial-gradient(white 1px, transparent 1px);

    background-size: 50px 50px;

    opacity: 0.12;

    animation:
        moveStars 120s linear infinite,
        pulseStars 8s ease-in-out infinite;

    z-index: -1;
}

@keyframes moveStars {

    from {
        transform: translateY(0px);
    }

    to {
        transform: translateY(-2000px);
    }
}

@keyframes pulseStars {

    0% {
        opacity: 0.08;
    }

    50% {
        opacity: 0.18;
    }

    100% {
        opacity: 0.08;
    }
}

/* REMOVE STREAMLIT DEFAULTS */

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

/* PAGE PADDING */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* TITLES */

.main-title {
    font-size: 58px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(90deg, #ffffff, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: floatTitle 6s ease-in-out infinite;
}

@keyframes floatTitle {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-6px);
    }

    100% {
        transform: translateY(0px);
    }
}

.sub-text {
    color: #94a3b8;
    font-size: 20px;
    margin-bottom: 30px;
}

/* GLASS CONTAINERS */

.chart-card {
    background: rgba(15, 23, 42, 0.45);
    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 18px;

    backdrop-filter: blur(16px);

    box-shadow: 0 8px 40px rgba(0,0,0,0.35);

    margin-bottom: 25px;

    transition: 0.3s;
}

.chart-card:hover {
    transform: translateY(-5px);
    border: 1px solid #38bdf8;
    box-shadow: 0 0 25px rgba(56,189,248,0.35);
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    background: rgba(15, 23, 42, 0.45);
    border-radius: 18px;
    padding: 10px;
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #38bdf8;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# ======================================================
# CLEANING
# ======================================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# ======================================================
# HEADER
# ======================================================

st.markdown("""
<div class="main-title">
Sales Analytics
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-text">
Deep operational insights and advanced business intelligence.
</div>
""", unsafe_allow_html=True)

# ======================================================
# ROW 1
# ======================================================

col1, col2 = st.columns(2)

# CATEGORY PERFORMANCE

with col1:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    category_sales = (
        df.groupby("Category")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    fig_category = px.bar(
        category_sales,
        x="Category",
        y=["Sales", "Profit"],
        barmode="group",
        title="Category Performance",
        template="plotly_dark",
        height=450
    )

    fig_category.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# SEGMENT ANALYSIS

with col2:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig_segment = px.pie(
        segment_sales,
        names="Segment",
        values="Sales",
        title="Customer Segment Contribution",
        template="plotly_dark",
        hole=0.6
    )

    fig_segment.update_layout(
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# ROW 2
# ======================================================

col3, col4 = st.columns(2)

# DISCOUNT VS PROFIT

with col3:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig_discount = px.scatter(
        df,
        x="Discount",
        y="Profit",
        color="Category",
        title="Discount vs Profit Analysis",
        template="plotly_dark",
        opacity=0.7,
        height=450
    )

    fig_discount.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(
        fig_discount,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# SHIPPING MODE

with col4:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    ship_mode = (
        df.groupby("Ship Mode")["Profit"]
        .sum()
        .reset_index()
    )

    fig_ship = px.bar(
        ship_mode,
        x="Ship Mode",
        y="Profit",
        color="Profit",
        title="Profit by Shipping Mode",
        template="plotly_dark",
        height=450
    )

    fig_ship.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(
        fig_ship,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# LOSS PRODUCTS
# ======================================================

st.markdown('<div class="chart-card">', unsafe_allow_html=True)

loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .reset_index()
    .sort_values(by="Profit")
    .head(10)
)

st.markdown("""
<h3 style='color:white;'>
Top Loss-Making Products
</h3>
""", unsafe_allow_html=True)

st.dataframe(
    loss_products,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)
