import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import ploty.express as px

st.set_page_config (layout="wide")

st.title("Dashboard")
st.header("LLM Data", divider='green')
st.subheader("**_Status:_** LLM 2")
st.write("current")
st.text("Jun 5, 2024")
status = st.checkbox("use local data?")
if status:
    st.info("local session data")

else:
    st.warning("_not enabled_")

df = pd.read_csv("aidata.csv")
st.write(df)
#st.dataframe(df, width = 1200 , height = 300)

st.subheader("**_chart:_** plot")

data = pd.read_csv('aidata.csv')

# Streamlit app title
st.title("AI Model Performance Scatter Plot")

# Select columns for scatter plot axes
columns = data.columns[1:]

# Dropdowns for selecting benchmarks
x_axis = st.selectbox('Select X-axis', columns)
y_axis = st.selectbox('Select Y-axis', columns)

# Scatter plot
fig, ax = plt.subplots(figsize=(6, 4))  # Adjust figsize to reduce the size by 50%
ax.scatter(data[x_axis], data[y_axis])

# Add labels and title
ax.set_xlabel(x_axis, fontsize=7)
ax.set_ylabel(y_axis, fontsize=7)
ax.set_title(f'Scatter Plot: {x_axis} vs {y_axis}', fontsize=8)

# Display plot in Streamlit
st.pyplot(fig)