import streamlit as st
import requests
import pandas as pd
import datetime
import time
from auto_mail import send_mail
st.set_page_config(page_title="cheran_app", layout="wide", page_icon="🅿️")

st.header("Wishing Happy Birthday 🎂🎂")


# Calculate time until midnight
now = datetime.datetime.now()
midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
time_until_midnight = (midnight - now).seconds
print(time_until_midnight)
# Wait until midnight
# time.sleep(time_until_midnight)
st.write(time_until_midnight)

st.header("hello there")
