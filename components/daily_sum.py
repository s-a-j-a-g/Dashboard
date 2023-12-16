import streamlit as st
import plotly.express as px
import pandas as pd


def daily_sum(filtered_df):
    # filtered_df["month_year"] = filtered_df["Date"].dt.to_period("M")
    # st.subheader("Time Series Analysis")

    # linechart = pd.DataFrame(
    #     filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y: %b"))["Cases"].sum()
    # ).reset_index()
    # fig2 = px.line(
    #     linechart,
    #     x="month_year",
    #     y="Cases",
    #     labels={"Cases": "Amount"},
    #     height=500,
    #     width=1000,
    #     template="gridon",
    # )
    # st.plotly_chart(fig2, use_container_width=True)

    # Assuming "Date" is a datetime column in your DataFrame
    filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])

    # Extract the day from the "Date" column and create a new column "day"
    filtered_df["day"] = filtered_df["Date"].dt.to_period("D").dt.strftime("%Y-%m-%d")

    # Display a subheader indicating the start of the time series analysis section
    st.subheader("Time Series Analysis")

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
        title="Time Series Analysis - Daily Sum of COVID-19 Cases",
        xaxis_title="Day",
        yaxis_title="Sum of Cases",
    )

    # Display the line chart using Streamlit
    st.plotly_chart(fig2, use_container_width=True)

    # filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])
    # filtered_df["day"] = filtered_df["Date"].dt.to_period("D")

    # # filtered_df["month_year"] = filtered_df["Date"].dt.to_period("M")
    # st.subheader("Time Series Analysis")

    # linechart = pd.DataFrame(
    #     filtered_df.groupby(filtered_df["day"].dt.strftime("%Y-%m-%d"))["Cases"].sum()
    # ).reset_index()
    # fig2 = px.line(
    #     linechart,
    #     x="day",
    #     y="Cases",
    #     labels={"Cases": "Amount"},
    #     height=500,
    #     width=1000,
    #     template="gridon",
    # )
    # st.plotly_chart(fig2, use_container_width=True)

    ### time series plot ##
    # st.title("Time Series Plot with Streamlit")
    # y_column = st.selectbox("Select Y-axis Column:",df.columns)
    # try:
    #     df[y_column]=pd.to_numeric(df[y_column])
    # except (ValueError,TypeError):
    #     st.warning(f"Column '{y_column}' contains mixed or incompatible types.Plz  Select another column")

    # x_column=st.selectbox("Select X-axis Column:",df.columns)
    # st.line_chart(df.set_index('Date'))
