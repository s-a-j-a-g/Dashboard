import streamlit as st
import plotly.express as px
import pandas as pd


def daily_sum(filtered_df):
    st.subheader("Time Series Analysis of Active Cases")

    # Assuming "Date" is a datetime column in your DataFrame
    filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])

    # Extract the day from the "Date" column and create a new column "day"
    filtered_df["day"] = filtered_df["Date"].dt.to_period("D").dt.strftime("%Y-%m-%d")

    # Group the DataFrame by the "day" column, calculate the sum of "Cases" for each day,
    # and reset the index to obtain a DataFrame suitable for plotting
    linechart = pd.DataFrame(filtered_df.groupby("day")["Cases"].sum()).reset_index()

    # Create a line chart using Plotly Express
    fig2 = px.line(
        linechart,
        x="day",
        y="Cases",
        labels={"Cases": "Sum of Cases for the Day"},
        height=500,
        width=1000,
        template="gridon",
    )

    # Customize the layout if needed
    fig2.update_layout(
        title="Daily COVID-19 Cases",
        xaxis_title="Day",
        yaxis_title="No. of Cases",
    )

    # Display the line chart using Streamlit
    st.plotly_chart(fig2, use_container_width=True)
