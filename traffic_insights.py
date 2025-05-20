import streamlit as st
import pandas as pd
import plotly.express as px
from data_generator import generate_flight_data

def show_traffic_insights():
    st.title("Traffic Insights")
    
    flights = generate_flight_data()
    
    st.subheader("Flight Traffic Analysis by Hour")
    flights['hour'] = flights['departure_time'].dt.hour
    hourly_traffic = flights.groupby('hour').size()
    st.line_chart(hourly_traffic)

    st.subheader("Top 10 Busiest Routes")
    busiest_routes = flights.groupby(['origin', 'destination']).size().nlargest(10).reset_index(name='flights')
    st.dataframe(busiest_routes)

    fig = px.bar(busiest_routes, x='origin', y='flights', color='destination')
    st.plotly_chart(fig)
