import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("energy_data_india.csv")

# Sidebar
st.sidebar.title("Filter Data")
regions = ["All"] + sorted(df["Region"].unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

# Filter data
if selected_region != "All":
    df = df[df["Region"] == selected_region]

st.title("India Energy Production Dashboard")

# Scatter Plot
st.subheader("Scatter Plot: Year vs Production")
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x="Year", y="Production", hue="Energy_Source")
st.pyplot(plt.gcf())
plt.clf()

# Line Graph
st.subheader("Line Graph: Energy Source Over Years")
line_data = df.groupby(["Year", "Energy_Source"])["Production"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=line_data, x="Year", y="Production", hue="Energy_Source", marker="o")
st.pyplot(plt.gcf())
plt.clf()

# Pie Chart
st.subheader("Pie Chart: Energy Source Share")
pie_data = df.groupby("Energy_Source")["Production"].sum()
fig, ax = plt.subplots()
ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)
