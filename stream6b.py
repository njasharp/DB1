import streamlit as st
import pandas as pd


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
