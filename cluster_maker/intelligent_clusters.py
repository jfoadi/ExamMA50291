import pandas as pd
import numpy as np
from dataframe_builder import define_dataframe_structure, simulate_data

def create_well_separated_clusters(seed_df, n_points=100, separation=10, col_specs=None, random_state=None):

    # Set random seed for reproducibility
    if random_state is not None:
        np.random.seed(random_state)

    # Adjust the centers of the groups by applying the separation
    separated_centers = seed_df.copy()
    for col in seed_df.columns:
        separated_centers[col] = seed_df[col] + np.arange(len(seed_df)) * separation

    # Simulate data points around the adjusted centers
    simulated_data = simulate_data(separated_centers, n_points=n_points, col_specs=col_specs, random_state=random_state)


    return simulated_data

