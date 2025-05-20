import streamlit as st
import pandas as pd
import plotly.express as px
from data_generator import generate_airport_data, generate_flight_data

def show_dashboard():
    st.title("Top 100 Airports - Dashboard")

    airport_data = generate_airport_data()
    flight_data = generate_flight_data()

    # Plot an interactive map of the airports
    st.subheader("Interactive Map of Airports")
    fig = px.scatter_geo(
        airport_data,
        lat='latitude',
        lon='longitude',
        hover_name='name',
        size='passenger_traffic',
        projection='natural earth'
    )
    st.plotly_chart(fig)

    st.subheader("Heatmap of Flight Traffic")
    heatmap_data = flight_data.groupby('origin').size().reset_index(name='flights')
    fig = px.density_heatmap(heatmap_data, x='origin', y='flights', color_continuous_scale='Viridis')
    st.plotly_chart(fig)
