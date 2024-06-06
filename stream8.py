import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv('mena_games.csv')

# Streamlit app title
st.title("MENA Games Market Analysis")

# Filter options
platforms = data['Platform'].unique()
regions = data['Region'].unique()
metrics = ['Downloads', 'Revenue', 'Avg. Weekly Hours','Esports Participation']

selected_platform = st.selectbox('Select Platform', platforms)
selected_region = st.selectbox('Select Region', regions)
selected_metric = st.selectbox('Select Metric', metrics)

# Filter data based on selections
filtered_data = data[(data['Platform'] == selected_platform) & (data['Region'] == selected_region)]

# Create charts
st.subheader(f"{selected_platform} Games in {selected_region} - {selected_metric}")

# Bar Chart
fig_bar = px.bar(filtered_data, x='Game', y=selected_metric, color='Game',
                 title=f"{selected_platform} Games in {selected_region} - {selected_metric} Bar Chart")
st.plotly_chart(fig_bar)

# Pie Chart
fig_pie = px.pie(filtered_data, names='Game', values=selected_metric, 
                 title=f"{selected_platform} Games in {selected_region} - {selected_metric} Distribution")
st.plotly_chart(fig_pie)

# Scatter Plot
fig_scatter = px.scatter(filtered_data, x='Game', y=selected_metric, size=selected_metric, color='Game',
                         title=f"{selected_platform} Games in {selected_region} - {selected_metric} Scatter Plot")
st.plotly_chart(fig_scatter)

# Line Chart (if data over time is available)
if 'Date' in filtered_data.columns:
    fig_line = px.line(filtered_data, x='Date', y=selected_metric, color='Game',
                       title=f"{selected_platform} Games in {selected_region} - {selected_metric} Over Time")
    st.plotly_chart(fig_line)
    
st.subheader('Data 2024 ')
image_path = "d-market.png"
st.image(image_path, caption='Info', use_column_width=True)