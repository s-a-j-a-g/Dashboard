import streamlit as st
import pandas as pd
import plotly.express as px


# def total_cases(filtered_df):
#     # Pie chart for case distribution by country/region
#     st.subheader(f"Case Distribution")

#     # totalCases = pd.DataFrame(
#     #     filtered_df.groupby("Country_Region")["Cases"].sum()
#     # ).reset_index()

#     fig = px.pie(
#         filtered_df,
#         values="Cases",
#         # names="Country_Region",
#         names="Province_State",
#         # title=f"Case Distribution for {selected_region}",
#     )

#     # Display the pie chart
#     st.plotly_chart(fig, use_container_width=True)


# def total_cases(filtered_df):
#     # Pie chart for case distribution by province/state
#     st.subheader(f"Case Distribution")

#     # Group by and sum the cases for each province/state
#     totalCases = pd.DataFrame(
#         filtered_df.groupby("Province_State")["Cases"].sum()
#     ).reset_index()

#     # Calculate the percentage of cases for each province/state
#     totalCases["Percentage"] = totalCases["Cases"] / totalCases["Cases"].sum() * 100

#     # Identify provinces/states with less than 3% of the total cases and group them into "Other"
#     totalCases["Province_State"] = totalCases["Province_State"].where(
#         totalCases["Percentage"] >= 3, "Other"
#     )

#     # Sum the cases for the grouped provinces/states
#     groupedCases = totalCases.groupby("Province_State")["Cases"].sum().reset_index()

#     # Create a pie chart
#     fig = px.pie(
#         groupedCases,
#         values="Cases",
#         names="Province_State",
#         title="Case Distribution by Province/State",
#     )

#     # Display the pie chart
#     st.plotly_chart(fig, use_container_width=True)


def total_cases(filtered_df):
    # Pie chart for case distribution by province/state
    st.subheader("Confirmed Cases Distribution by Country")

    # Group by and sum the cases for each province/state
    totalCases = pd.DataFrame(
        filtered_df.groupby("Country_Region")["Cases"].sum()
    ).reset_index()

    # Calculate the percentage of cases for each province/state
    totalCases["Percentage"] = totalCases["Cases"] / totalCases["Cases"].sum() * 100

    # Identify provinces/states with less than 3% of the total cases and group them into "Other"
    totalCases["Country_Region"] = totalCases["Country_Region"].where(
        totalCases["Percentage"] >= 2, "Other"
    )

    # Sum the cases for the grouped provinces/states
    groupedCases = totalCases.groupby("Country_Region")["Cases"].sum().reset_index()

    # Create a pie chart
    fig = px.pie(
        groupedCases,
        values="Cases",
        names="Country_Region",
        # title="Case Distribution by Country_Region/State",
    )

    # Display the pie chart
    st.plotly_chart(fig, use_container_width=True)
