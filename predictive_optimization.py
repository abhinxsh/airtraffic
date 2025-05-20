import streamlit as st
import pandas as pd
import numpy as np
from data_generator import generate_flight_data
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def show_predictive_optimization():
    st.title("Predictive Optimization")
    
    flights = generate_flight_data()
    flights['hour'] = flights['departure_time'].dt.hour
    hourly_traffic = flights.groupby('hour').size()

    # Time-series forecasting using Exponential Smoothing
    model = ExponentialSmoothing(hourly_traffic, seasonal='add', seasonal_periods=24)
    model_fit = model.fit()
    forecast = model_fit.forecast(24)
    
    st.subheader("Hourly Traffic Forecast for Next 24 Hours")
    st.line_chart(forecast)

    st.subheader("Optimization Recommendations")
    st.write("Based on the forecast, adjust flight schedules to reduce peak congestion.")
