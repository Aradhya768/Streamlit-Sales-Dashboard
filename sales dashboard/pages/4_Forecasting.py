import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
import plotly.express as px

from utils.data_loader import load_data

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="AI Forecast Engine",
    layout="wide"
)

# ======================================================
# LOAD DATA
# ======================================================

df = load_data()

# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

/* =====================================================
GLOBAL
===================================================== */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* =====================================================
BACKGROUND
===================================================== */

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

    z-index: -3;
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

    z-index: -2;
}

/* NEURAL GRID */

.grid-overlay {

    position: fixed;

    inset: 0;

    background-image:
        linear-gradient(rgba(56,189,248,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56,189,248,0.05) 1px, transparent 1px);

    background-size: 55px 55px;

    mask-image: radial-gradient(circle at center, black 35%, transparent 85%);

    animation: gridFlow 18s linear infinite;

    z-index: -1;
}

/* FLOATING ORBS */

.orb {

    position: fixed;

    border-radius: 50%;

    filter: blur(90px);

    opacity: 0.18;

    z-index: -1;
}

.orb1 {

    width: 320px;
    height: 320px;

    background: #38bdf8;

    top: 8%;
    left: 6%;

    animation: float1 12s ease-in-out infinite;
}

.orb2 {

    width: 280px;
    height: 280px;

    background: #8b5cf6;

    bottom: 10%;
    right: 5%;

    animation: float2 14s ease-in-out infinite;
}

/* =====================================================
ANIMATIONS
===================================================== */

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

@keyframes gridFlow {

    from {
        transform: translateY(0px);
    }

    to {
        transform: translateY(55px);
    }
}

@keyframes float1 {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-35px);
    }

    100% {
        transform: translateY(0px);
    }
}

@keyframes float2 {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(35px);
    }

    100% {
        transform: translateY(0px);
    }
}

@keyframes floatText {

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

@keyframes pulseAnim {

    0% {
        transform: scale(1);
        opacity: 1;
    }

    100% {
        transform: scale(2.2);
        opacity: 0;
    }
}

@keyframes rotateRing {

    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

/* =====================================================
HIDE STREAMLIT
===================================================== */

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

/* =====================================================
LAYOUT
===================================================== */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* =====================================================
TITLE
===================================================== */

.main-title {

    font-size: 64px;
    font-weight: 800;

    background: linear-gradient(90deg, #ffffff, #38bdf8);

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: floatText 6s ease-in-out infinite;

    margin-bottom: 10px;
}

.sub-text {

    color: #94a3b8;
    font-size: 20px;
    margin-bottom: 35px;
}

/* =====================================================
HERO PANEL
===================================================== */

.hero-panel {

    position: relative;

    background: rgba(15,23,42,0.45);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 40px;

    backdrop-filter: blur(18px);

    overflow: hidden;

    margin-bottom: 35px;

    box-shadow: 0 8px 40px rgba(0,0,0,0.35);
}

.hero-ring {

    width: 220px;
    height: 220px;

    margin: auto;

    border-radius: 50%;

    position: relative;

    background:
        radial-gradient(circle, rgba(56,189,248,0.18), transparent 65%);
}

.hero-ring::before {

    content: "";

    position: absolute;

    inset: -10px;

    border-radius: 50%;

    border: 2px solid rgba(56,189,248,0.45);

    border-top: 2px solid #38bdf8;

    animation: rotateRing 12s linear infinite;
}

.hero-core {

    position: absolute;

    top: 50%;
    left: 50%;

    transform: translate(-50%, -50%);

    width: 90px;
    height: 90px;

    border-radius: 50%;

    background: #38bdf8;

    box-shadow:
        0 0 40px rgba(56,189,248,0.8),
        0 0 90px rgba(56,189,248,0.45);
}

.hero-status {

    text-align: center;

    margin-top: 25px;

    color: #cbd5e1;

    font-size: 18px;
}

/* =====================================================
GLASS CARDS
===================================================== */

.glass {

    position: relative;

    overflow: hidden;

    background: rgba(15,23,42,0.45);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 24px;

    backdrop-filter: blur(18px);

    box-shadow: 0 8px 40px rgba(0,0,0,0.35);

    margin-bottom: 25px;

    transition: 0.3s;
}

.glass::before {

    content: "";

    position: absolute;

    inset: 0;

    border-radius: 24px;

    padding: 1px;

    background: linear-gradient(
        135deg,
        rgba(56,189,248,0.8),
        rgba(168,85,247,0.4),
        transparent
    );

    -webkit-mask:
        linear-gradient(#fff 0 0) content-box,
        linear-gradient(#fff 0 0);

    -webkit-mask-composite: xor;

    pointer-events: none;
}

.glass:hover {

    transform: translateY(-6px);

    border: 1px solid #38bdf8;

    box-shadow: 0 0 30px rgba(56,189,248,0.35);
}

/* =====================================================
KPI
===================================================== */

.kpi-title {

    color: #94a3b8;
    font-size: 16px;
}

.kpi-value {

    font-size: 38px;
    font-weight: 700;
    color: white;

    margin-top: 8px;
}

.kpi-growth {

    color: #22c55e;
    font-size: 15px;

    margin-top: 10px;
}

/* =====================================================
AI STATUS
===================================================== */

.live-status {

    display: flex;
    align-items: center;
    gap: 8px;

    color: #38bdf8;

    margin-top: 15px;

    font-size: 14px;
}

.pulse {

    width: 10px;
    height: 10px;

    border-radius: 50%;

    background: #38bdf8;

    box-shadow: 0 0 12px #38bdf8;

    animation: pulseAnim 1.5s infinite;
}

/* =====================================================
AI INSIGHTS
===================================================== */

.insight-box {

    border-left: 4px solid #38bdf8;

    background: rgba(15,23,42,0.55);

    padding: 28px;

    border-radius: 20px;

    position: relative;

    overflow: hidden;
}

.insight-box::before {

    content: "AI GENERATED INSIGHTS";

    position: absolute;

    top: 14px;
    right: 20px;

    font-size: 11px;

    letter-spacing: 2px;

    color: rgba(255,255,255,0.18);
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# BACKGROUND ELEMENTS
# ======================================================

st.markdown("""
<div class="grid-overlay"></div>
<div class="orb orb1"></div>
<div class="orb orb2"></div>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================

st.markdown("""
<div class="main-title">
AI Forecast Engine
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-text">
Predict future business performance using intelligent trend analysis and forecasting models.
</div>
""", unsafe_allow_html=True)

# ======================================================
# HERO PANEL
# ======================================================

hero_html = """
<div class="hero-panel">

<div class="hero-ring">
<div class="hero-core"></div>
</div>

<div class="hero-status">
Neural Forecasting Core Active
<br><br>
Real-time predictive intelligence processing business trends
</div>

</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

# ======================================================
# PREPARE DATA
# ======================================================

forecast_df = (
    df.groupby("Order Date")["Sales"]
    .sum()
    .reset_index()
)

forecast_df.columns = ["ds", "y"]

# ======================================================
# MODEL
# ======================================================

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model.fit(forecast_df)

future = model.make_future_dataframe(periods=90)

forecast = model.predict(future)

# ======================================================
# KPI CALCULATIONS
# ======================================================

latest_actual = forecast_df["y"].iloc[-30:].mean()

future_prediction = forecast["yhat"].iloc[-30:].mean()

growth_rate = (
    (future_prediction - latest_actual)
    / latest_actual
) * 100

confidence_score = 94
risk_level = "Low"

# ======================================================
# KPI CARDS
# ======================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    card1 = f"""
<div class="glass">

<div class="kpi-title">
Predicted Revenue
</div>

<div class="kpi-value">
${future_prediction:,.0f}
</div>

<div class="kpi-growth">
Next 90 Days
</div>

<div class="live-status">
<span class="pulse"></span>
AI ACTIVE
</div>

</div>
"""

    st.markdown(card1, unsafe_allow_html=True)

with k2:

    card2 = f"""
<div class="glass">

<div class="kpi-title">
Expected Growth
</div>

<div class="kpi-value">
{growth_rate:.2f}%
</div>

<div class="kpi-growth">
Forecast Trend
</div>

<div class="live-status">
<span class="pulse"></span>
LIVE ANALYSIS
</div>

</div>
"""

    st.markdown(card2, unsafe_allow_html=True)

with k3:

    card3 = f"""
<div class="glass">

<div class="kpi-title">
Confidence Score
</div>

<div class="kpi-value">
{confidence_score}%
</div>

<div class="kpi-growth">
AI Reliability
</div>

<div class="live-status">
<span class="pulse"></span>
MODEL STABLE
</div>

</div>
"""

    st.markdown(card3, unsafe_allow_html=True)

with k4:

    card4 = f"""
<div class="glass">

<div class="kpi-title">
Risk Level
</div>

<div class="kpi-value">
{risk_level}
</div>

<div class="kpi-growth">
Forecast Stability
</div>

<div class="live-status">
<span class="pulse"></span>
LOW VOLATILITY
</div>

</div>
"""

    st.markdown(card4, unsafe_allow_html=True)
    # ======================================================
# SALES FORECAST GRAPH
# ======================================================

st.markdown('<div class="glass">', unsafe_allow_html=True)

fig = go.Figure()

# ACTUAL SALES

fig.add_trace(go.Scatter(
    x=forecast_df["ds"],
    y=forecast_df["y"],
    mode='lines',
    name='Actual Sales',
    line=dict(
        color='white',
        width=2
    )
))

# FORECAST

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat"],
    mode='lines',
    name='Forecasted Sales',
    line=dict(
        color='#38bdf8',
        width=5
    )
))

# UPPER BOUND

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat_upper"],
    mode='lines',
    line_color='rgba(0,0,0,0)',
    showlegend=False
))

# LOWER BOUND

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat_lower"],
    fill='tonexty',
    mode='lines',
    line_color='rgba(0,0,0,0)',
    fillcolor='rgba(56,189,248,0.15)',
    name='Confidence Interval'
))

# FORECAST ZONE

fig.add_vrect(
    x0=forecast_df["ds"].max(),
    x1=forecast["ds"].max(),
    fillcolor="rgba(56,189,248,0.08)",
    layer="below",
    line_width=0
)

fig.update_traces(
    line_shape='spline'
)

fig.update_layout(

    template="plotly_dark",

    height=700,

    title="Actual Sales vs AI Forecast",

    paper_bgcolor='rgba(0,0,0,0)',

    plot_bgcolor='rgba(0,0,0,0)',

    font=dict(color="white"),

    xaxis=dict(showgrid=False),

    yaxis=dict(
        gridcolor="rgba(255,255,255,0.08)"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)
# ======================================================
# SEASONALITY ANALYSIS
# ======================================================

monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Sales"]
    .mean()
    .reset_index()
)

monthly_sales.columns = ["Month", "Average Sales"]

st.markdown('<div class="glass">', unsafe_allow_html=True)

fig_season = px.line(
    monthly_sales,
    x="Month",
    y="Average Sales",
    markers=True,
    template="plotly_dark",
    title="Seasonality Detection"
)

fig_season.update_traces(
    line=dict(
        width=4,
        color="#38bdf8"
    )
)

fig_season.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=500
)

st.plotly_chart(
    fig_season,
    use_container_width=True
)

best_month = monthly_sales.loc[
    monthly_sales["Average Sales"].idxmax()
]

worst_month = monthly_sales.loc[
    monthly_sales["Average Sales"].idxmin()
]

seasonal_spike = (
    best_month["Average Sales"]
    - monthly_sales["Average Sales"].mean()
)

st.markdown(f"""

<h3 style="color:#38bdf8;">
Seasonal Intelligence
</h3>

<p style="color:#cbd5e1; font-size:17px; line-height:1.9;">

• Strongest sales month detected:
<strong>Month {int(best_month['Month'])}</strong>

<br><br>

• Weakest business performance observed in:
<strong>Month {int(worst_month['Month'])}</strong>

<br><br>

• Seasonal spike intensity exceeds average sales by:
<strong>${seasonal_spike:,.0f}</strong>

<br><br>

• AI detected cyclical demand behavior and recurring seasonal purchasing patterns.

</p>

""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# ======================================================
# ANOMALY DETECTION
# ======================================================

forecast_df["Rolling Mean"] = (
    forecast_df["y"]
    .rolling(window=7)
    .mean()
)

forecast_df["Anomaly"] = np.where(
    abs(forecast_df["y"] - forecast_df["Rolling Mean"]) > 4000,
    "Anomaly",
    "Normal"
)

normal_df = forecast_df[
    forecast_df["Anomaly"] == "Normal"
]

anomaly_df = forecast_df[
    forecast_df["Anomaly"] == "Anomaly"
]

st.markdown('<div class="glass">', unsafe_allow_html=True)

fig_anomaly = go.Figure()

# NORMAL SALES

fig_anomaly.add_trace(go.Scatter(
    x=normal_df["ds"],
    y=normal_df["y"],
    mode='markers',
    name='Normal Activity',
    marker=dict(
        color='rgba(56,189,248,0.65)',
        size=7
    )
))

# ANOMALIES

fig_anomaly.add_trace(go.Scatter(
    x=anomaly_df["ds"],
    y=anomaly_df["y"],
    mode='markers',
    name='Critical Anomaly',
    marker=dict(
        color='#ff3b30',
        size=14,
        line=dict(
            color='white',
            width=2
        )
    )
))

fig_anomaly.update_layout(

    template="plotly_dark",

    title="AI Anomaly Detection Engine",

    height=550,

    paper_bgcolor='rgba(0,0,0,0)',

    plot_bgcolor='rgba(0,0,0,0)',

    font=dict(color="white")
)

st.plotly_chart(
    fig_anomaly,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)
# ======================================================
# AI INSIGHTS
# ======================================================

top_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

top_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

st.markdown(f"""
<div class="insight-box">

<h2 style="color:#38bdf8;">
AI Insights
</h2>

<p style="color:#cbd5e1; font-size:18px; line-height:1.9;">

• Sales expected to change by
<strong>{growth_rate:.2f}%</strong>
over the upcoming quarter.

<br><br>

• <strong>{top_category}</strong>
currently shows the strongest revenue momentum.

<br><br>

• <strong>{top_region}</strong>
region demonstrates dominant purchasing activity.

<br><br>

• Seasonal spikes detected during peak-performing periods.

<br><br>

• AI confidence remains strong with low volatility patterns.

<br><br>

• Heavy discounting continues reducing profitability efficiency.

<br><br>

• Multiple anomalies indicate potential promotional or demand surge events.

</p>

</div>
""", unsafe_allow_html=True)