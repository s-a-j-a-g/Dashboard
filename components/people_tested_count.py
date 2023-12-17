import streamlit as st
import plotly.express as px


def people_tested_count(filtered_df):
    st.subheader("People Total Tested Count")

    n = 10  # Adjust this value based on your needs
    downsampled_df = filtered_df.iloc[::n, :]

    fig = px.bar(
        # filtered_df,
        downsampled_df,
        x="Date",
        y="People_Total_Tested_Count",
        labels={"People_Total_Tested_Count": "Total People Tested", "Date": "Date"},
        # title="Testing Metrics Over Time",
    )

    # Update layout for better readability
    fig.update_layout(xaxis_title="Date", yaxis_title="Total People Tested")

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
