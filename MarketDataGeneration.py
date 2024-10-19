import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to generate growth data points based on initial size and CAGR
def generate_growth_data(current_size, cagr, start_year, projection_years):
    data_points = []
    for year in range(start_year, start_year + projection_years + 1):
        market_size = current_size * ((1 + cagr) ** (year - start_year))
        data_points.append((year, market_size))
    return data_points


# Industry Data (Based on Market Research)
industries = {
    "Brain Computer Interface (BCI)": {"current_size": 1500, "start_year": 2020, "projected_size": 3500, "projected_year": 2026, "cagr": 0.17},
    "Neuromorphic Computing": {"current_size": 50, "start_year": 2021, "projected_size": 475, "projected_year": 2026, "cagr": 0.45},
    "GPU Industry": {"current_size": 25000, "start_year": 2021, "projected_size": 92000, "projected_year": 2026, "cagr": 0.40},
    "AI Accelerated Chips": {"current_size": 10000, "start_year": 2021, "projected_size": 70000, "projected_year": 2026, "cagr": 0.45},
    "Quantum Computing": {"current_size": 500, "start_year": 2021, "projected_size": 3000, "projected_year": 2026, "cagr": 0.45},
    "Compute for Advanced Robotics": {"current_size": 2000, "start_year": 2021, "projected_size": 5000, "projected_year": 2026, "cagr": 0.20},
    "Neuroprosthetics": {"current_size": 7000, "start_year": 2021, "start_year": 2021, "projected_size": 14000, "projected_year": 2026, "cagr": 0.14},
    "General Stem Cell": {"current_size": 14000, "start_year": 2021, "projected_size":26400, "projected_year": 2026, "cagr": 0.14},
    "Adult Stem Cells": {"current_size": 8500, "start_year": 2021, "projected_size": 14500, "projected_year": 2026, "cagr": 0.12},
    "Induced Pluripotent Stem Cells": {"current_size": 1200, "start_year": 2021, "projected_size": 2800, "projected_year": 2026, "cagr": 0.20},
    "Embryonic Stem Cells": {"current_size": 500, "start_year": 2021, "projected_size": 1100, "projected_year": 2026, "cagr": 0.11},
    "Perinatal Stem Cells": {"current_size": 1000, "start_year": 2021, "projected_size": 1800, "projected_year": 2026, "cagr": 0.14},
    "Optogenetic Therapeutics": {"current_size": 30, "start_year": 2021, "projected_size": 250, "projected_year": 2026, "cagr": 0.60},
    "Optogenetic Diagnostics": {"current_size": 90, "start_year": 2021, "projected_size": 450, "projected_year": 2026, "cagr": 0.42},
}

years = 10  # Number of years to simulate

# Initialize a dictionary to store all data
all_data = {'Year': range(2021, 2021 + years + 1)}

# Plotting each industry on a logarithmic scale (for sanity purposes)
plt.figure(figsize=(12, 8))

# Loop through each industry and add its market size data to the dictionary
for industry, data in industries.items():
    current_size = data['current_size']
    start_year = data['start_year']
    cagr = data['cagr']
    
    # Generate growth data
    growth_data = generate_growth_data(current_size, cagr, start_year, years)
    
    # Extract just the market size for the respective years and add it to the dictionary
    market_sizes = [size for _, size in growth_data]
    
    # Use the industry name as the column name
    all_data[industry] = market_sizes

# Convert the dictionary to a DataFrame
df_all_markets = pd.DataFrame(all_data)

# Save the combined data to a CSV file
df_all_markets.to_csv("./data/MarketProjectionData.csv", index=False)