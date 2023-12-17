import plotly.express as px
import streamlit as st


def create_country_bar_chart(filtered_df):
    # Assuming country_df is the DataFrame with grouped data
    country_df = filtered_df.groupby(
        by=["Country_Region", "Case_Type"], as_index=False
    )["Cases"].sum()

    # Filter for only Confirmed and Death case types
    filtered_country_df = country_df[
        country_df["Case_Type"].isin(["Confirmed", "Deaths"])
    ]

    # Calculate the sum of cases for each country
    country_totals = (
        filtered_country_df.groupby("Country_Region")["Cases"].sum().reset_index()
    )

    # Get the top 20 countries based on the total sum of cases
    top_10_countries = country_totals.nlargest(10, "Cases")["Country_Region"].tolist()

    # Filter the data for the top 20 countries
    filtered_country_df_top10 = filtered_country_df[
        filtered_country_df["Country_Region"].isin(top_10_countries)
    ]

    st.subheader("Top 10 Country: Confirmed and Death Cases")
    fig = px.bar(
        filtered_country_df_top10,
        x="Country_Region",
        y="Cases",
        color="Case_Type",  # Use color to distinguish between Confirmed and Death cases
        text=["{:,}".format(x) for x in filtered_country_df_top10["Cases"]],
        template="seaborn",
        barmode="group",  # Use "group" mode for grouped bars
    )
    st.plotly_chart(fig, use_container_width=True, height=600)
