import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

def train_time_series_model(data, seasonal_periods=24):
    """
    Trains an Exponential Smoothing model on the provided time-series data.
    
    Parameters:
    - data: pandas Series of time-series data
    - seasonal_periods: number of periods in a seasonal cycle (e.g., 24 for hourly data)
    
    Returns:
    - model_fit: Fitted time-series model
    - forecast: Forecasted values for the next 24 periods
    """
    model = ExponentialSmoothing(data, seasonal='add', seasonal_periods=seasonal_periods)
    model_fit = model.fit()
    forecast = model_fit.forecast(seasonal_periods)
    return model_fit, forecast

def plot_time_series(data, forecast):
    """
    Plots the original time-series data and the forecast.
    
    Parameters:
    - data: pandas Series of historical data
    - forecast: pandas Series of forecasted data
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.values, label='Historical Data')
    plt.plot(forecast.index, forecast.values, label='Forecast', linestyle='--')
    plt.legend()
    plt.title("Time-Series Forecast")
    plt.xlabel("Time")
    plt.ylabel("Traffic Volume")
    plt.grid(True)
    plt.show()

def calculate_performance_metrics(flights):
    """
    Calculates key performance metrics like delays and cancellation rates.
    
    Parameters:
    - flights: DataFrame with flight data including delay and cancellation columns
    
    Returns:
    - Dictionary containing metrics like average delay, cancellation rate, and on-time performance
    """
    avg_delay = flights['delay'].mean()
    cancellation_rate = flights['cancellation'].mean() * 100
    on_time_performance = (flights['delay'] == 0).mean() * 100
    return {
        "avg_delay": avg_delay,
        "cancellation_rate": cancellation_rate,
        "on_time_performance": on_time_performance
    }