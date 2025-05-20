import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from data_generator import generate_flight_data

def show_performance_analytics():
    st.title("Performance Analytics")
    
    # Generate synthetic flight data
    flights = generate_flight_data()
    
    # Simulate delay data (in minutes)
    np.random.seed(42)
    flights['delay'] = np.random.choice([0, 15, 30, 45, 60], size=len(flights), p=[0.6, 0.2, 0.1, 0.05, 0.05])
    flights['cancellation'] = np.random.choice([0, 1], size=len(flights), p=[0.95, 0.05])
    
    # Delay Analysis
    st.subheader("Average Delay Analysis")
    avg_delay = flights.groupby('origin')['delay'].mean().reset_index()
    fig_delay = px.bar(avg_delay, x='origin', y='delay', title='Average Delay by Airport')
    st.plotly_chart(fig_delay)

    # Cancellation Analysis
    st.subheader("Cancellation Rates")
    cancellation_rate = flights['cancellation'].mean() * 100
    st.metric("Overall Cancellation Rate", f"{cancellation_rate:.2f}%")

    # On-time Performance
    st.subheader("On-Time Performance")
    on_time_performance = (flights['delay'] == 0).mean() * 100
    st.metric("On-Time Flights", f"{on_time_performance:.2f}%")

    # Top Delayed Routes
    st.subheader("Top 10 Most Delayed Routes")
    delayed_routes = flights[flights['delay'] > 0].groupby(['origin', 'destination'])['delay'].mean().nlargest(10).reset_index()
    st.dataframe(delayed_routes)

if __name__ == "__main__":
    show_performance_analytics()
