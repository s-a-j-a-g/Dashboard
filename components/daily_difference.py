import streamlit as st
import plotly.express as px


def daily_difference(filtered_df):
    # Calculate daily differences in confirmed cases
    filtered_df["Daily_Differences"] = filtered_df["Cases"].diff()

    st.subheader(f"Daily Differences in Confirmed Cases")

    fig = px.bar(
        filtered_df,
        x="Date",
        y="Daily_Differences",
        labels={"Daily_Differences": "Daily Differences", "Date": "Date"},
        # title=f"Daily Differences in Confirmed Cases for {selected_region}",
    )

    fig.update_layout(xaxis_title="Date", yaxis_title="Daily Differences")

    st.plotly_chart(fig, use_container_width=True)
