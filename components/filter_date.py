import streamlit as st
import pandas as pd


def filter_date(df):
    col1, col2 = st.columns((2))
    df["Date"] = pd.to_datetime(df["Date"])

    # Get the min and max date
    startDate = pd.to_datetime(df["Date"]).min()
    endDate = pd.to_datetime(df["Date"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

    df = df[(df["Date"] >= date1) & (df["Date"] <= date2)].copy()
    return df


# df["Date"] = pd.to_datetime(df["Date"])

# # Get the min and max date
# startDate = pd.to_datetime(df["Date"]).min()
# endDate = pd.to_datetime(df["Date"]).max()

# with col1:
#     date1 = pd.to_datetime(st.date_input("Start Date", startDate))

# with col2:
#     date2 = pd.to_datetime(st.date_input("End Date", endDate))

# df = df[(df["Date"] >= date1) & (df["Date"] <= date2)].copy()
