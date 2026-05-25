def calculate_kpis(df):

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order ID"].nunique()

    avg_order_value = total_sales / total_orders

    profit_margin = (total_profit / total_sales) * 100

    return {
        "sales": total_sales,
        "profit": total_profit,
        "orders": total_orders,
        "avg_order_value": avg_order_value,
        "profit_margin": profit_margin
    }