import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Dashboard", layout="wide")

st.title("📊 Retail Sales Dashboard")

df = pd.read_csv("retail.csv")

st.dataframe(df.head())

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", int(df["Sales"].sum()))
col2.metric("Total Profit", int(df["Profit"].sum()))
col3.metric("Total Quantity", int(df["Quantity"].sum()))

st.subheader("Sales by Category")
fig = px.bar(df, x="Category", y="Sales")
st.plotly_chart(fig, use_container_width=True)

df["Order Date"] = pd.to_datetime(df["Order Date"])
sales_time = df.groupby("Order Date")["Sales"].sum().reset_index()

st.subheader("Sales Over Time")
fig2 = px.line(sales_time, x="Order Date", y="Sales")
st.plotly_chart(fig2, use_container_width=True)
