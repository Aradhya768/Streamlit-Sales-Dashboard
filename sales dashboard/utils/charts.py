import plotly.express as px

def monthly_sales_chart(df):

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    monthly_sales["Month"] = monthly_sales["Month"].astype("category")

    monthly_sales["Month"] = monthly_sales["Month"].cat.set_categories(
        month_order,
        ordered=True
    )

    monthly_sales = monthly_sales.sort_values("Month")

    fig = px.line(
        monthly_sales,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    return fig