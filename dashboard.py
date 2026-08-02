from datetime import datetime
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Premium Sales Dashboard",
    page_icon="📊",
    layout="wide"
)
theme = st.sidebar.radio(
    "🎨 Select Theme",
    ["Dark", "Light"]
)
if theme == "Dark":

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }

        [data-testid="stSidebar"] {
            background-color: #1C1F26;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F5F7FA;
            color: black;
        }

        [data-testid="stSidebar"] {
            background-color: #EAECEF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.caption("Built with ❤️ using Python, Pandas and Streamlit")
st.sidebar.image(
    "logo.png",
    width=180
)
st.sidebar.title("⚙️ Dashboard Controls")

st.sidebar.info(
    """
    👨‍💻 Developer: Ahmad Yar

    📊 Project: Sales Analytics Dashboard

    🚀 Built with Python & Streamlit
    """
)

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #1f4037, #99f2c8);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: white;
    ">
        <h1>📊 Sales Analytics Dashboard</h1>
        <h3>Real-Time Business Insights & Performance Tracking</h3>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div style="text-align:right; color:#A9A9A9;">
        📅 {datetime.now().strftime("%d %B %Y")} <br>
        ⏰ {datetime.now().strftime("%I:%M %p")}
    </div>
    """,
    unsafe_allow_html=True
)

df = pd.read_csv("sales_data.csv")
st.write(df.columns)
st.sidebar.subheader("🔍 Filters")
search_product = st.sidebar.text_input(
    "🔎 Search Product"
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].unique())
)
selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + list(df["Product"].unique())
)

if selected_category != "All":
    df = df[df["Category"] == selected_category]
if selected_product != "All":
    df = df[df["Product"] == selected_product]
if search_product:
    df = df[
        df["Product"].str.contains(
            search_product,
            case=False
        )
    ]

with st.expander("📋 View Sales Data"):
    st.dataframe(df)
df["Total_Sales"] = df["Quantity"] * df["Price"]

total_sales = df["Total_Sales"].sum()
total_orders = df["OrderID"].count()
best_category = df.groupby("Category")["Total_Sales"].sum().idxmax()
top_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div style="
            background-color:#1E88E5;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
        ">
            <h4>💰 Total Sales</h4>
            <h2>{total_sales}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="
            background-color:#43A047;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
        ">
            <h4>🏆 Best Category</h4>
            <h2>{best_category}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="
            background-color:#FB8C00;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
        ">
            <h4>⭐ Top Product</h4>
            <h2>{top_product}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div style="
            background-color:#8E24AA;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
        ">
            <h4>📦 Total Orders</h4>
            <h2>{total_orders}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
category_sales = df.groupby("Category")["Total_Sales"].sum()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

left, right = st.columns(2)

with left:
    st.subheader("📊 Category-wise Sales")
    st.bar_chart(category_sales)

with right:
    st.subheader("🥧 Sales Distribution")
    st.pyplot(fig)

top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
sales_trend = df.groupby("Product")["Total_Sales"].sum()

left, right = st.columns(2)

with left:
    st.subheader("🏆 Top 3 Products")
    st.table(top_products)

with right:
    st.subheader("📈 Sales Trend")
    st.line_chart(sales_trend)


st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📈 Sales Progress")

st.progress(85)

st.write("85% of monthly sales target achieved")
current_sales = total_sales
target_sales = 10000

percentage = int((current_sales / target_sales) * 100)

st.write(f"🎯 Target Completion: {percentage}%")
st.subheader("📋 Dashboard Summary")

st.write(f"📦 Total Orders: {total_orders}")

st.write(f"💰 Total Revenue: {total_sales}")

st.write(f"🏆 Best Category: {best_category}")

st.write(f"⭐ Top Product: {top_product}")

st.markdown("---")

st.markdown(
    """
    <hr>
    <center>
    👨‍💻 Developed by Ahmad Yar <br>
    Python • Pandas • Streamlit • Data Analytics 🚀
    </center>
    """,
    unsafe_allow_html=True
)
with open("sales_report.xlsx", "rb") as file:
    st.download_button(
        label="📥 Download Excel Report",
        data=file,
        file_name="sales_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

