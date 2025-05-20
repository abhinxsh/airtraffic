import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from data_generator import generate_airport_data, generate_flight_data

def show_network_analysis():
    st.title("Network Analysis")
    
    airports = generate_airport_data()
    flights = generate_flight_data()
    
    G = nx.Graph()
    for _, flight in flights.iterrows():
        G.add_edge(flight["origin"], flight["destination"])
    
    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_size=50, node_color="skyblue")
    st.pyplot(plt)

if __name__ == "__main__":
    show_network_analysis()
