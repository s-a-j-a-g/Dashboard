import streamlit as st
import plotly.express as px


def population_vs_cases(filtered_df):
    # Scatter plot for Population vs. Cases
    st.subheader(f"Population vs. Confirmed Cases")

    subsampled_df = filtered_df.sample(n=min(1000, len(filtered_df)))

    fig = px.scatter(
        subsampled_df,
        x="Population_Count",
        y="Cases",
        text="Combined_Key",
        log_x=True,
        log_y=True,
        # title="Population vs. Confirmed Cases",
        labels={"Population_Count": "Population", "Cases": "Confirmed Cases"},
        opacity=0.7,  # Set transparency for better visibility
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
