import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="cheran_app", layout="wide", page_icon="🅿️")
st.header("Dashboard")
st.write("this is some text")
st.write("this is automation mail feature available")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Value1", 3434)
with col2:
    st.metric("Value2", 546456)
with col3:
    st.metric("Value3", 7868)

res = requests.get("https://fakestoreapi.com/products")
data = res.json()
df = pd.DataFrame(data)
st.dataframe(df)

grouped_data = df.groupby("category")["price"].sum()

st.header("hi sona this is prathap")
st.write("hey there sona!!!!! i love you")
st.bar_chart(data=grouped_data, height=200, width=200, use_container_width=True)
# st.balloons()
st.snow()
