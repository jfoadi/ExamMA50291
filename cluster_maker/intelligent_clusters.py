import pandas as pd
import numpy as np
from cluster_maker import simulate_data

def create_separated_clusters(df, points = 1000, col_specs = None, separation = 100, random_state = None):
    """
    Create well-separated clusters based on a seed DataFrame.

    Parameters:
        df (pd.DataFrame): Seed DataFrame with representative points.
        points (int): Number of points to generate per representative.
        col_specs (dict, optional): Specifications for column-wise data simulation.
        separation (int): Minimum distance to separate clusters.
        random_state (int, optional): Seed for random number generation.

    Returns:
        pd.DataFrame: DataFrame containing the simulated data points.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input provided should be seed dataframe created by define_dataframe_structure")
    if col_specs is not None and not isinstance(col_specs, dict):
        raise TypeError("Col_specs provided should be of a dictionary type")
    if not isinstance(separation, int) or separation <= 0:
        raise TypeError("Separation provided should be a positive integer")
    if random_state is not None and not isinstance(random_state, int):
        raise TypeError("Random_state should be an integer")
    if not isinstance(points, int) or points <= 0:
        raise TypeError("Points should be a positive integer")
    
    if random_state is not None:
        np.random.seed(random_state)

    # df of separated seed dataframe
    adjusted_seed_dataframe = df.copy()
    for i, col in enumerate(adjusted_seed_dataframe.columns):
        # we want to randomise separation factor while also making sure that the clusters are well spaced from each other with no overlap

        rand_separation = separation + np.random.uniform(0, separation)
        adjusted_seed_dataframe[col] = adjusted_seed_dataframe[col] + i * rand_separation
    
    generated_data = simulate_data(adjusted_seed_dataframe, points, col_specs, random_state)
    
    return generated_data

