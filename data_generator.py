import pandas as pd
import numpy as np

def generate_airport_data(num_airports=100):
    np.random.seed(42)
    airports = []
    for i in range(num_airports):
        airport = {
            "id": i,
            "name": f"Airport {i}",
            "city": f"City {i}",
            "country": f"Country {i % 10}",
            "latitude": np.random.uniform(-90, 90),
            "longitude": np.random.uniform(-180, 180),
            "passenger_traffic": np.random.randint(500_000, 10_000_000)
        }
        airports.append(airport)
    return pd.DataFrame(airports)

def generate_flight_data(num_flights=2000, num_airports=100):
    np.random.seed(42)
    peak_hours = [7, 8, 9, 18, 19, 20]  # Morning and evening rush hours
    flights = []
    for i in range(num_flights):
        departure_hour = np.random.choice(peak_hours if np.random.rand() < 0.5 else range(24))
        flight = {
            "flight_id": f"FL{i}",
            "origin": np.random.randint(0, num_airports),
            "destination": np.random.randint(0, num_airports),
            "duration": np.random.randint(60, 600),
            "distance": np.random.randint(100, 10000),
            "departure_time": pd.Timestamp.now() + pd.to_timedelta(departure_hour, unit='h')
        }
        flights.append(flight)
    return pd.DataFrame(flights)
