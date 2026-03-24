import streamlit as st
import pandas as pd
 
st.write("""
# BITCOIN
Bitcoin as a function of *time!*
""")
 
#df = pd.read_csv("my_data.csv")
df = pd.read_csv("data/btcusd_1-min_data.csv")
st.line_chart(df["High"])

