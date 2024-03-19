import streamlit as st
import requests
import pandas as pd


st.set_page_config(hide_streamlit_style=True)
st.set_page_config(page_title="cheran_app",layout="wide", page_icon="🅿️" )
st.header("Dashboard")
st.write("this is some text")
st.write("this is automation mail feature available")

res = requests.get("https://fakestoreapi.com/products")
data = res.json()
df = pd.DataFrame(data)
st.dataframe(df)

grouped_data = df.groupby("category")["price"].sum()

st.header("hi sona this is prathap")
st.write("hey there sona!!!!! i love you")
st.bar_chart(data=grouped_data,height=200,width=200,use_container_width=True)
# st.balloons()
st.snow()