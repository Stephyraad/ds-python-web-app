import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('./vehicles_us.csv')

st.header('Vehicle Dashboard', divider="gray")

# Histogram of price distribution
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Scatter plot of price vs. model year
fig_scatter = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
st.plotly_chart(fig_scatter)

# Checkbox to filter by automatic transmission
if st.checkbox('Show only automatic transmission'):
    df = df[df['transmission'] == 'automatic']

    # Update plots with filtered data
    fig_hist = px.histogram(df, x='price', title='Price Distribution (Automatic only)')
    st.plotly_chart(fig_hist)

    fig_scatter = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year (Automatic only)')
    st.plotly_chart(fig_scatter)
