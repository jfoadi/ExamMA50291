from cluster_maker import define_dataframe_structure, simulate_data
import pandas as pd

def create_separated_clusters(seed_df, n_points=100, separation=10, random_state=None):
    
    # Modify the seed DataFrame to ensure well-separated groups
    separated_df = seed_df.copy()
    for i, col in enumerate(separated_df.columns):
        separated_df[col] += i * separation  # Increment each column to ensure separation

    # Simulate data based on the modified seed DataFrame
    col_specs = {
        col: {'distribution': 'normal', 'variance': separation / 2} for col in separated_df.columns
        }
    simulated_data = simulate_data(separated_df, n_points=n_points, col_specs=col_specs, random_state=random_state)

    return simulated_data