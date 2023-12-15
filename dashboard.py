import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import os
import warnings
from components.top_10_countrywise_bargraph import create_country_bar_chart
from components.filter_date import filter_date


warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="COVID-19 Global Case and Death Visualization", page_icon=":bar_chart:", layout="wide"
)

st.title(" :bar_chart: COVID-19 Global Case and Death Visualization")
st.markdown(
    "<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True
)

fl = st.file_uploader(
    ":file_folder: Upload a File", type=(["csv", "txt", "xlsx", "xls"])
)

if fl is not None:
    fileName = fl.name
    st.write(fileName)
    df = pd.read_csv(fileName, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\saakar\Desktop\Projects\Data_Mining\Mini_project\Dashboard/Assets")
    df = pd.read_csv("covid-19_cases.csv", encoding="ISO-8859-1")

# Date input with column ######################################
col1, col2 = st.columns((2))
# # df = filter_date(df.copy())
df["Date"] = pd.to_datetime(df["Date"]) 

# Get the min and max date
startDate = pd.to_datetime(df["Date"]).min()
endDate = pd.to_datetime(df["Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))


# Logic for start date & end date#
df = df[(df["Date"] >= date1) & (df["Date"] <= date2)].copy()

##############################################################

filtered_df = df

with col2:
    st.subheader("COVID-19 Status")
    fig = px.pie(filtered_df, values="Cases", names="Case_Type", hole=0.5)
    fig.update_traces(text=filtered_df["Case_Type"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)


create_country_bar_chart(filtered_df)

### time series plot ##
# st.title("Time Series Plot with Streamlit")
# y_column = st.selectbox("Select Y-axis Column:",df.columns)
# try:
#     df[y_column]=pd.to_numeric(df[y_column])
# except (ValueError,TypeError):
#     st.warning(f"Column '{y_column}' contains mixed or incompatible types.Plz  Select another column")

# x_column=st.selectbox("Select X-axis Column:",df.columns)
# st.line_chart(df.set_index('Date'))

def plot_time_series(df):
    st.title("Time Series Plot with Streamlit")

    # Select y-axis column
    y_column = st.selectbox("Select Y-axis Column:", df.columns)

    # Attempt to convert the selected y-axis column to numeric
    try:
        df[y_column] = pd.to_numeric(df[y_column])
    except (ValueError, TypeError):
        st.warning(f"Column '{y_column}' contains mixed or incompatible types. Please select another column.")
        return

    # Select x-axis column (assuming it's 'Date' in this case)
    x_column = st.selectbox("Select X-axis Column:", df.columns)

    # Display time series plot
    st.line_chart(df.set_index(x_column)[y_column])

plot_time_series(df)