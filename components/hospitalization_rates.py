import streamlit as st
import plotly.express as px
import pandas as pd


def hospitalization_rates(filtered_df):
    # st.subheader("Cumulative Hospitalization Count Over Time")
    st.subheader("Hospitalization Count Over Time")

    filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])

    # Extract the day from the "Date" column and create a new column "day"
    filtered_df["day"] = filtered_df["Date"].dt.to_period("D").dt.strftime("%Y-%m-%d")

    # Group the DataFrame by the "day" column, calculate the sum of "Cases" for each day,
    # and reset the index to obtain a DataFrame suitable for plotting
    linechart = pd.DataFrame(
        filtered_df.groupby("day")["People_Hospitalized_Cumulative_Count"].sum()
    ).reset_index()

    # Create a line chart using Plotly Express
    fig2 = px.line(
        linechart,
        x="day",
        y="People_Hospitalized_Cumulative_Count",
        labels={"Cases": "Sum of Cases for the Day"},
        height=500,
        width=1000,
        template="gridon",
    )

    # Customize the layout if needed
    fig2.update_layout(
        xaxis_title="Day",
        yaxis_title="Hospitalized Population",
    )

    # Display the line chart using Streamlit
    st.plotly_chart(fig2, use_container_width=True)
