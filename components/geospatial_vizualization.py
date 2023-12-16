import streamlit as st
import plotly.express as px
import pandas as pd


def geospatial_visualizer(filtered_df):
    st.subheader("Geospatial Distribution of Confirmed Cases")

    filtered_df = filtered_df.head(1000)

    # totalCases = pd.DataFrame(
    #     filtered_df.groupby("Country_Region")["Cases"].sum()
    # ).reset_index()

    # totalCases_subset = totalCases.head(100)

    fig = px.scatter_geo(
        filtered_df,
        lat="Lat",
        lon="Long",
        hover_name="Combined_Key",
        # text="Country_Region",
        size="Cases",
        projection="natural earth",
        height=800,
    )

    # Update layout for better readability
    fig.update_layout(geo=dict(showland=True))
    fig.update_geos(
        projection_type="natural earth",
        showland=True,
        landcolor="LightGreen",
        showocean=True,
        oceancolor="LightBlue",
    )

    # Display the map
    st.plotly_chart(fig, use_container_width=True)
