import streamlit as st
import pandas as pd
import plotly.express as px

# Set the default layout to wide
st.set_page_config(page_title="MENA Games Market Analysis", page_icon=":video_game:", layout="centered")

# Enable dark mode
st.markdown("<style>body {background-color: #212121;}</style>", unsafe_allow_html=True)
# Load data
data = pd.read_csv('mena_games.csv')

# Custom CSS to hide the Streamlit menu and footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)



# Streamlit app title
st.title("MENA Games Market Analysis")
st.divider()

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
- By 2028, the market is projected to approach nearly 100 billion ($97.1 billion) with a CAGR of 2.5%.

### Top Items:

- The number of gamers in Asia & MENA was 1.61 billion in 2023, over half of the world’s total gamers.
- India is projected to contribute 72% of the growth in gamers, adding 277 million new gamers by 2028.
- The MENA region is expected to be the second fastest growing market.
- Mobile gaming dominates with 93.7% of gamers playing on mobile devices.
- By 2028, there will be an estimated 1.87 billion mobile gamers, 606 million PC gamers, and 100 million console gamers.

“Asia and MENA remain critical in the global games market, and drivers to the growth in these regions include localization, increase in participation by female gamers, government support for esports, growth of out-of-app monetization of mobile games, and rising spending power.” said Lisa Hanson, CEO of Niko Partners. “In order to gain meaningful access, companies must get to know the local market realities and clearly understand the context behind the data they use for their strategic planning.”

The Middle East and North Africa region has catapulted into the spotlight as a formidable force in the mobile gaming industry, showcasing unparalleled potential and breakneck development. In fact, mobile gaming is currently the region’s major game industry growth driver. Leading this charge are the UAE and Saudi Arabia - both pivotal markets are turbocharging the mobile gaming boom. With cutting-edge technology, a dynamic youth population, and escalating disposable incomes, these nations are not just participating but are at the epicenter of a gaming revolution. Their influence is propelling the entire region forward, making MENA a hub of innovation and growth in the global mobile gaming arena. 

Gamesforum delves into the ​​current state of mobile gaming in the region, exploring market size, growth trends, and the factors propelling this industry forward, with insight from industry leaders.

# MENA Mobile Gaming Industry Overview

## Region's Growth
- The Middle East and North Africa (MENA) region is rapidly becoming a major player in the mobile gaming industry, driven by technological advancements and a dynamic youth population.

## Key Markets
- The UAE and Saudi Arabia are leading the charge, with significant contributions to the region's growth.

## Technological Influence
- Cutting-edge technology, including AR, VR, cloud gaming, and 5G, is fueling industry expansion.

## Economic Factors
- Increasing disposable incomes and high smartphone penetration are major growth drivers.

# Market Size and Trends

## Market Expansion
- Egypt, the UAE, and Saudi Arabia are the premier markets, expected to reach nearly 80 million users by 2027.

## Popular Games
- **MENA-3 Region**: PUBG, EA Sports FC, and Call of Duty.
- **General**: Candy Crush Saga, Subway Surfers, and Yalla Ludo.

## Government Support
- Dubai's Gaming Visa initiative aims to attract 30,000 game developers, boosting the local economy.

# Country-Specific Growth

## Jordan
- Projected to reach $48 million in revenue by 2024, with 2.1 million users by 2027.

## Egypt
- Mobile gaming sector growing by 25% annually, supported by increasing smartphone adoption.

# Increasing Smartphone Penetration

## High Penetration Rates
- UAE and Saudi Arabia have smartphone penetration rates exceeding 90%.

## Accessibility
- Affordable smartphones make gaming accessible to a broad audience, boosting demand and market growth.

# Gaming Preferences and Habits

## Youth and Teenagers
- Prefer competitive and interactive games like PUBG Mobile and Fortnite.

## Young Adults
- Favor strategic and long-term engagement games like Clash of Clans and Call of Duty: Mobile.

## Female Gamers
- Increasing numbers drawn to casual and puzzle games like Candy Crush Saga and Ludo King.

# Monetisation Challenges

## Payment Systems
- Diversity in payment systems and reliance on cash transactions pose barriers.

## High Transaction Fees
- Erode profit margins for developers.

## Local Preferences
- Companies need to integrate multiple payment gateways to cater to local preferences, adding complexity and cost.

# Summary Table

| Country            | Key Growth Drivers                       | Popular Games                        |
|--------------------|------------------------------------------|--------------------------------------|
| UAE & Saudi Arabia | High smartphone penetration, youth population | PUBG, EA Sports FC, Call of Duty     |
| Jordan             | Young population, government support     | Candy Crush Saga, Subway Surfers, Yalla Ludo |
| Egypt              | Increasing smartphone adoption           | PUBG, Clash of Clans, Mobile Legends |

This concise summary captures the key points about the MENA region's mobile gaming industry, highlighting growth trends, market size, gaming preferences, and monetisation challenges.
https://www.globalgamesforum.com/features/mobile-gaming-in-mena-growth-trends-and-a-future-outlook/?/mobile%2dgaming%2din%2dmena%2dgrowth%2dtrends%2dand%2da%2dfuture%2doutlook%2f#:~:text=The%20mobile%20gaming%20market%20in,a%20lucrative%20market%20for%20developers.
"""





st.markdown(report_text)
st.info("built by DW 6-24-24 - v1.2")