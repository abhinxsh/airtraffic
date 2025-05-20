import streamlit as st
from dashboard_module import show_dashboard
from network_analysis import show_network_analysis
from traffic_insights import show_traffic_insights
from performance_analytics import show_performance_analytics
from predictive_optimization import show_predictive_optimization

# Streamlit Sidebar for Navigation
st.sidebar.title("Air Traffic Analysis & Optimization")
page = st.sidebar.selectbox(
    "Select Module", 
    ["Dashboard", "Network Analysis", "Traffic Insights", "Performance Analytics", "Predictive Optimization"]
)

# Main Content Based on Selection
try:
    if page == "Dashboard":
        show_dashboard()
    elif page == "Network Analysis":
        show_network_analysis()
    elif page == "Traffic Insights":
        show_traffic_insights()
    elif page == "Performance Analytics":
        show_performance_analytics()
    elif page == "Predictive Optimization":
        show_predictive_optimization()
except Exception as e:
    st.error(f"An error occurred: {e}") 