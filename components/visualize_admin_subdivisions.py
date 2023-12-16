import streamlit as st
import pandas as pd
import plotly.express as px


def visualize_admin_subdivisions(filtered_df):
    st.subheader(f"Total Cases by Admin2")

    # Group by and sum the cases for each administrative subdivision
    totalCases = pd.DataFrame(
        filtered_df.groupby("Admin2")["Cases"].sum()
    ).reset_index()

    # Create a bar chart
    fig = px.bar(
        totalCases,
        x="Admin2",
        y="Cases",
        text="Cases",
        # title=f"Total Cases by {}",
    )

    # Update layout for better readability
    fig.update_layout(xaxis_title=f"Admin2", yaxis_title="Total Cases")

    # Display the bar chart
    st.plotly_chart(fig, use_container_width=True)
