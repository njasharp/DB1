import streamlit as st
import pandas as pd
import plotly.express as px

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

# Load data
data = pd.read_csv('aidata.csv')

# Streamlit app title
st.title("AI Model Performance Scatter Plot")

# Select columns for scatter plot axes
columns = data.columns[1:]

# Dropdowns for selecting benchmarks
x_axis = st.selectbox('Select X-axis', columns)
y_axis = st.selectbox('Select Y-axis', columns)

# Scatter plot
fig = px.scatter(data, x=x_axis, y=y_axis, color=data.index,
                 title=f'Scatter Plot: {x_axis} vs {y_axis}')
# Add labels and title with increased font size
fig.update_layout(
    title_font_size=24,
    xaxis_title=x_axis,
    yaxis_title=y_axis,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Display plot in Streamlit
st.plotly_chart(fig)