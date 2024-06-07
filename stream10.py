import streamlit as st
import pandas as pd
import plotly.express as px

# Set the default layout to wide
st.set_page_config(page_title="SEA-6 Gaming Market Analysis", page_icon=":video_game:", layout="centered")

# Enable dark mode
st.markdown("<style>body {background-color: #212121;}</style>", unsafe_allow_html=True)
# Load data
data = pd.read_csv('sea_games.csv')

# Streamlit app title
st.title("SEA-6 Gaming Market Analysis")
st.header("Dashboard", divider='red')

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
    
st.subheader('Asia & MENA Gaming Markets ')
image_path = "d-market.png"
st.image(image_path, caption='Data 2024 -https://venturebeat.com/games/niko-partners-mena-asia-market-report-2024/', use_column_width=True)

st.header('Niko Partners Report on Asia & MENA Gaming Markets')

# Display the report text
report_text = """
### Key Updates:

- The combined revenue for Asia & MENA gaming markets was $85.5 billion in 2023, marking a 4.6% increase from the previous year.
- For 2024, the forecasted growth rate is 2.5%, with expected revenue reaching $87.6 billion.
- By 2028, the market is projected to approach nearly 100 billion (97.1 billion) with a CAGR of 2.5%.

### Top Items:

- The number of gamers in Asia & MENA was 1.61 billion in 2023, over half of the world’s total gamers.
- India is projected to contribute 72% of the growth in gamers, adding 277 million new gamers by 2028.
- The MENA region is expected to be the second fastest growing market.
- Mobile gaming dominates with 93.7% of gamers playing on mobile devices.
- By 2028, there will be an estimated 1.87 billion mobile gamers, 606 million PC gamers, and 100 million console gamers.

“Asia and MENA remain critical in the global games market, and drivers to the growth in these regions include localization, increase in participation by female gamers, government support for esports, growth of out-of-app monetization of mobile games, and rising spending power.” said Lisa Hanson, CEO of Niko Partners. “In order to gain meaningful access, companies must get to know the local market realities and clearly understand the context behind the data they use for their strategic planning.”

### Key Insights:
Revenue Projections: The SEA-6 region's gaming market is projected to reach 5.8 billion in 2023, with an expected increase to 7.2 billion by 2027. Mobile gaming dominates the market, accounting for 66% of the revenue, which is expected to grow to 70% by 2027​ (GamesIndustry.biz)​​ (Pocket Gamer)​.

### Esports Growth: 
The esports market within the SEA-6 region is also growing, with significant participation rates across various games. The region's unique cultural diversity means each country has different preferences and trends in gaming​ (Mobile Marketing Reads)​​ (Niko Partners)​.

### Popular Games and Platforms: 
Mobile games like Mobile Legends and Garena Free Fire are highly popular, with high download rates and revenue. PC games like League of Legends and Dota 2 also see significant engagement, especially in esports. Console gaming, while less dominant, has a strong presence with games like FIFA 22 and Call of Duty: Warzone​ (Newzoo)​.

This data provides a comprehensive overview of the current gaming trends and statistics in the SEA-6 region. For more detailed reports and insights, you can refer to sources like Niko Partners and Newzoo.

### Key Insights and Sources

#### Market Growth: 
The SEA-6 region, including Vietnam and Malaysia, continues to see significant growth in gaming, driven primarily by mobile gaming. The market is expected to see further growth in the coming years.
#### Esports Participation: 
Esports is a major component of the gaming ecosystem in these countries, with substantial participation rates and viewership.
#### Popular Games and Genres: 
Mobile Legends, Free Fire, PUBG Mobile, and Genshin Impact are among the most popular games across these regions. On PC, games like League of Legends, Dota 2, and Valorant dominate, while console gamers prefer FIFA, Call of Duty, and Fortnite.
These data points are based on a combination of sources including Newzoo and Niko Partners. For more detailed and up-to-date statistics, refer to their respective reports and market analyses.
"""

st.markdown(report_text)
st.info("built by DW 6-8-24 - v1")