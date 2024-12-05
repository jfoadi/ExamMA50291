import pandas as pd
import numpy as np
from .dataframe_builder import define_dataframe_structure, simulate_data
from .plot_clusters import plot_clusters
from .data_exporter import export_formatted, export_to_csv 

def intelligent_cluster_groups(column_specs, n_points=100, col_specs=None, group_separation_factor=1.0, random_state=42):
    """
    Function generates well separated clusters based on the inputted cluster centres.
    
    Parameters:
    Parameters:
        column_specs (list of dict): A list of dictionaries specifying the columns and their representative points.
            Example:
            [
                {'name': 'X', 'reps': [1, 5, 10]},
                {'name': 'Y', 'reps': [2, 6, 11]}
            ]
        n_points (int): The number of data points to simulate per cluster (default: 100).
        col_specs (dict, optional): A dictionary specifying the distribution and variance for data simulation.
            Example:
            {
                'X': {'distribution': 'normal', 'variance': 0.5},
                'Y': {'distribution': 'normal', 'variance': 0.5}
            }
        group_separation_factor (float): A multiplier that determines the degree of separation between cluster centers.
            - Values > 1: Increase separation between clusters.
            - Values < 1: Decrease separation between clusters.
        random_state (int, optional): A seed for random number generation to ensure reproducibility (default: 42).

    Returns:
        pd.DataFrame: A DataFrame containing the simulated data points with cluster labels.
        pdDataFrame: A DataFrame containing the cluster centers.
    
    """
    
    
    seed_df = define_dataframe_structure(column_specs) # creates seed dataframe showing the cluster centres
    
    # changes the cluster centres to be well separated.
    for i in seed_df.columns:
        col_mean = np.mean(seed_df[i]) # This calculates the mean of the inputted dataframe points
        seed_df[i] = col_mean + (seed_df[i] - col_mean) * group_separation_factor # by computing the difference between each value and the mean, multiplying by the separation factor creates well separated data points if separaion factor > 1.
    
    # This simulates data points around the changed cluster centres 
    data = simulate_data(seed_df, n_points=n_points, col_specs=col_specs, random_state=42)
    
    # Assign cluster labels based on the new cluster centre points
    number_of_clusters = len(seed_df)
    cluster_labels = []
    for cluster_number in range(number_of_clusters):
        cluster_labels.extend([cluster_number] * n_points)
    data['Cluster'] = cluster_labels

    return data, seed_df
