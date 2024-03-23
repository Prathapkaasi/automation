import streamlit as st
import requests
import pandas as pd
import datetime
import time
from auto_mail import send_mail

st.set_page_config(page_title="cheran_app", layout="wide", page_icon="🅿️")

pd.set_option("display.max_columns", 2)
pd.set_option("display.max_rows", 50)
df = pd.read_csv("bigdata.csv")

cleaned_df = df.dropna(subset=["DATE"], how="all")
cleaned_df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

# selected_creteria = st.selectbox(label="filter here", options=cleaned_df["Part Name"].unique())
# date_filter = st.date_input(label="date")
# selected_df = cleaned_df.query("`Part Name`==@selected_creteria & `DATE`==@date_filter")
cleaned_df["Part Name"] = cleaned_df["Part Name"].replace("-", "Missing")
cleaned_df["Part Name"] = cleaned_df["Part Name"].replace("0", "Missing")
cleaned_df["Part Name"] = cleaned_df["Part Name"].replace(0, "Missing")
cleaned_df["Part Name"] = cleaned_df["Part Name"].fillna("Missing")

filtered_df = cleaned_df[cleaned_df.notna()]
st.dataframe(filtered_df, height=500, use_container_width=True)

cleaned_df["Achive_Qty"] = pd.to_numeric(cleaned_df["Achive_Qty"], errors="coerce")
cleaned_df["Achive_Qty"] = cleaned_df["Achive_Qty"].astype(float)

month_wise_df = cleaned_df.groupby("Month")[["Total Rej.", "Plan QTY", "Achive_Qty", "Ok Qty"]].sum()
date_wise_df = cleaned_df.groupby("DATE")[["Total Rej.", "Plan QTY", "Achive_Qty", "Ok Qty"]].sum()





unique_vals = cleaned_df["Part Name"].unique().tolist()

col_config = {
    "Part Name": st.column_config.SelectboxColumn("New Part Name",
                                                  help="data invalid",
                                                  width="medium",
                                                  options=unique_vals, required=True)
}
st.data_editor(cleaned_df, column_config=col_config, use_container_width=True)
col1, col2 = st.columns(2)
st.divider()
# data_df = pd.DataFrame(
#     {
#         "category": [
#             "📊 Data Exploration",
#             "📈 Data Visualization",
#             "🤖 LLM",
#             "📊 Data Exploration",
#         ],
#     }
# )
# st.data_editor(
#     data_df,
#     column_config={
#         "category": st.column_config.SelectboxColumn(
#             "App Category",
#             help="The category of the app",
#             width="medium",
#             options=[
#                 "📊 Data Exploration",
#                 "📈 Data Visualization",
#                 "🤖 LLM",
#             ],
#             required=True,
#         )
#     },
#     hide_index=True,
# )
st.divider()

with col1:
    st.write("# Month Wise Summary")
    st.dataframe(month_wise_df, use_container_width=True)
    st.write("# Date Wise Summary")
    # Define CSS style for the border

    st.dataframe(date_wise_df, use_container_width=True)
with col2:
    st.write("# :blue[Chart Wise Summary]")
    st.bar_chart(month_wise_df, use_container_width=True, color=["#DA2033", "#BF620A", "#5D29EA", "#ffaa01"])
    st.write("# Describe Summary")

    st.dataframe(cleaned_df.describe(), use_container_width=True)
    # st.color_picker(label="color")
# Calculate time until midnight
# now = datetime.datetime.now()
# midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
# time_until_midnight = (midnight - now).seconds
# print(time_until_midnight)
# Wait until midnight
# time.sleep(time_until_midnight)
