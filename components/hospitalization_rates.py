import streamlit as st
import plotly.express as px


def hospitalization_rates(df):
    st.sidebar.title("Hospitalization Rates Over Time")

    st.sidebar.write("Select Region:")
    selected_region = st.sidebar.selectbox("Region", df["Country_Region"].unique())

    # Filter the DataFrame based on the selected region
    filtered_df = df[df["Country_Region"] == selected_region]

    # Line chart for cumulative count of people hospitalized over time
    st.subheader(f"Cumulative Hospitalization Count Over Time for {selected_region}")

    fig = px.line(
        filtered_df,
        x="Date",
        y="People_Hospitalized_Cumulative_Count",
        labels={
            "People_Hospitalized_Cumulative_Count": "Cumulative Hospitalization Count",
            "Date": "Date",
        },
        title=f"Cumulative Hospitalization Count Over Time for {selected_region}",
    )

    # Update layout for better readability
    fig.update_layout(
        xaxis_title="Date", yaxis_title="Cumulative Hospitalization Count"
    )

    # Display the line chart
    st.plotly_chart(fig, use_container_width=True)
