import streamlit as st
import plotly.express as px


# def population_vs_cases(filtered_df):
#     # Scatter plot for Population vs. Cases
#     st.subheader(f"Population Vs. Confirmed Cases")

#     subsampled_df = filtered_df.sample(n=min(1000, len(filtered_df)))

#     fig = px.scatter(
#         subsampled_df,
#         x="Population_Count",
#         y="Cases",
#         # text="Combined_Key",
#         log_x=True,
#         log_y=True,
#         # title="Population vs. Confirmed Cases",
#         labels={
#             "Population_Count": "Population",
#             "Cases": "Confirmed Cases",
#             # "Combined_Key": "Location",
#         },
#         opacity=0.7,  # Set transparency for better visibility
#     )

#     # Update layout for better readability
#     fig.update_layout(xaxis_title="Population", yaxis_title="Confirmed Cases")


#     # Display the scatter plot
#     st.plotly_chart(fig, use_container_width=True)


def population_vs_cases(filtered_df):
    # Combine the dataset for the same country by taking the sum of cases
    grouped_df = (
        filtered_df.groupby("Combined_Key")
        .agg({"Population_Count": "mean", "Cases": "sum"})
        .reset_index()
    )

    # Scatter plot for Population vs. Cases
    st.subheader(f"Population Vs. Confirmed Cases")

    subsampled_df = grouped_df.sample(n=min(1000, len(grouped_df)))

    fig = px.scatter(
        subsampled_df,
        x="Population_Count",
        y="Cases",
        log_x=True,
        log_y=True,
        labels={"Population_Count": "Population", "Cases": "Confirmed Cases"},
        hover_name="Combined_Key",
        opacity=0.7,
    )

    # Update layout for better readability
    fig.update_layout(xaxis_title="Population", yaxis_title="Confirmed Cases")

    # Display the scatter plot
    st.plotly_chart(fig, use_container_width=True)


# fig = px.scatter(
#     filtered_df,
#     x="Population_Count",
#     y="Cases",
#     text="Combined_Key",
#     log_x=True,  # Log-scale for better visualization if population counts vary widely
#     log_y=True,  # Log-scale for better visualization if case counts vary widely
#     # title="Population vs. Confirmed Cases",
#     labels={"Population_Count": "Population", "Cases": "Confirmed Cases"},
# )

# # Update layout for better readability
# fig.update_layout(xaxis_title="Population", yaxis_title="Confirmed Cases")

# # Display the scatter plot
# st.plotly_chart(fig, use_container_width=True)
