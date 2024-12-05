###
## Module intelligent_clusters.py
## Student 249290349 - University of Bath - 2024
###

## Libraries & modules needed
import numpy as np
import pandas as pd
import cluster_maker as cm
import cluster_maker.data_analyser as da

def sim_intelligent_data(seed_df, n_points=100, random_state=None, sep=10):
    """
    Simulate numerical data points around seed representatives, with column-specific distributions and variances.

    Parameters:
        seed_df (pd.DataFrame): DataFrame with numerical representative points (the "seed").
        n_points (int): Number of points to generate per representative.
        random_state (int, optional): Random seed for reproducibility.
        sep(float, int): separation distance (variance) between groups (default=10)

    Returns:
        Data (pd.DataFrame): DataFrame containing the data points.
        Correlation matrix, corr (pd.Dataframe).
    """
    try:
        if not isinstance(seed_df, pd.DataFrame):
            raise TypeError("seed_df must be a pandas DataFrame")
        if seed_df.empty:
            raise ValueError("seed_df must not be an empty DataFrame")
        
        #generate column specification with normal distibution and variance, sep.
        col_specs = {
            'name': {'distribution': 'normal', 'variance': sep},
        }
        #generate simulated data using the newly defined #col_specs
        data = cm.simulate_data(seed_df, n_points, col_specs, random_state)
        corr = da.calculate_correlation(data)
        
        return data, corr
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None