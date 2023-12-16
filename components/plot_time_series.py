import streamlit as st
import plotly.express as px
import pandas as pd


def plot_time_series(df):
    st.title("Time Series Plot with Streamlit")

    # Select y-axis column
    y_column = st.selectbox("Select Y-axis Column:", df.columns)

    # Attempt to convert the selected y-axis column to numeric
    try:
        df[y_column] = pd.to_numeric(df[y_column])
    except (ValueError, TypeError):
        st.warning(
            f"Column '{y_column}' contains mixed or incompatible types. Please select another column."
        )
        return

    # Select x-axis column (assuming it's 'Date' in this case)
    x_column = st.selectbox("Select X-axis Column:", df.columns)

    # Display time series plot
    st.line_chart(df.set_index(x_column)[y_column])
