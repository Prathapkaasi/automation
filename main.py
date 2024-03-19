import streamlit as st
import requests
import pandas as pd
st.set_page_config(page_title="cheran_app",layout="wide", page_icon="🅿️" )
st.header("Dashboard")
st.write("this is some text")
st.write("this is automation mail feature available")

res = requests.get("https://fakestoreapi.com/products")
data = res.json()
df = pd.DataFrame(data)
st.dataframe(df)

st.header("hi sona this is prathap")