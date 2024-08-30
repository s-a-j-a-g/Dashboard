import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
from components.top_10_countrywise_bargraph import create_country_bar_chart
from components.daily_sum import daily_sum
from components.geospatial_vizualization import geospatial_visualizer
from components.people_tested_count import people_tested_count
from components.total_cases import total_cases
from components.population_vs_cases import population_vs_cases
from components.daily_difference import daily_difference
from components.hospitalization_rates import hospitalization_rates


warnings.filterwarnings("ignore")

#########################################################
###################### Page Setup #######################
#########################################################
st.set_page_config(
    page_title="COVID-19 Global Case and Death Visualization",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title(" :bar_chart: COVID-19 Global Case and Death Visualization")
st.markdown(
    "<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True
)
#########################################################
#########################################################
#########################################################

#########################################################
################## Side Bar Uploader ####################
#########################################################
fl = st.sidebar.file_uploader(
    ":file_folder: Upload a File", type=(["csv", "txt", "xlsx", "xls"])
)
#########################################################
#########################################################
#########################################################

####### Select CSV File #######
if fl is not None:
    fileName = fl.name
    st.write(fileName)
    df = pd.read_csv(fileName, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\DELL\Documents\DevelopmentFiles\Data-Visualization\assets")
    # os.chdir(r"C:\Users\saakar\Desktop\Projects\Data_Mining\Mini_project\Dashboard/Assets")
    df = pd.read_csv("covid-19_cases.csv", encoding="ISO-8859-1")
    #########################################################

    ####### Get the Min and Max Date #######
    minDate = pd.to_datetime(df["Date"]).min()
    maxDate = pd.to_datetime(df["Date"]).max()
    #########################################################

    #########################################################
    ################## Side Bar Filter ######################
    #########################################################
    st.sidebar.title("Filter")
    startDate = pd.to_datetime(st.sidebar.date_input("Start Date", minDate))
    endDate = pd.to_datetime(st.sidebar.date_input("End Date", maxDate))
    #########################################################
    #########################################################
    #########################################################

    # Select Datas from Start Date and End Date
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[(df["Date"] >= startDate) & (df["Date"] <= endDate)].copy()
    #########################################################

    filtered_df = df

    col1, col2, col3 = st.columns((3))

    with col1:
        total_confirmed_cases = filtered_df["Cases"].sum()
        st.metric("Total", f"{total_confirmed_cases:,}", delta=0)

    with col2:
        total_confirmed_cases = filtered_df.loc[filtered_df['Case_Type'] == 'Confirmed', 'Cases'].sum()
        st.metric("Confirmed Cases", f"{ total_confirmed_cases:,}", delta=0)

    with col3:
        total_death_cases = filtered_df.loc[filtered_df['Case_Type'] == 'Deaths', 'Cases'].sum()
        st.metric("Deaths", f"{total_death_cases:,}", delta=0)

    col1, col2 = st.columns((2))

    with col1:
        total_cases(filtered_df)

    with col2:
        st.subheader("COVID-19 Status")
        fig = px.pie(filtered_df, values="Cases", names="Case_Type", hole=0.5)
        fig.update_traces(text=filtered_df["Case_Type"], textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    #########################################################
    #########################################################
    #########################################################
    daily_sum(filtered_df)
    create_country_bar_chart(filtered_df)
    # people_tested_count(filtered_df)
    geospatial_visualizer(filtered_df)
    population_vs_cases(filtered_df)
    hospitalization_rates(filtered_df)
    #########################################################
    #########################################################
    #########################################################

    #########################################################
    ############ Country Specific Visualization #############
    #########################################################
    st.title("Country Specific Visualization")

    col1, col2 = st.columns((2))
    with col1:
        selected_region = st.selectbox("Region", df["Country_Region"].unique())

    filtered_df = df[df["Country_Region"] == selected_region]

    daily_difference(filtered_df)
    # hospitalization_rates(filtered_df)
    # total_cases(filtered_df)
    #########################################################
    #########################################################
    #########################################################


    
