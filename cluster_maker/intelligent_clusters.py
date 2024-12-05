

import numpy as np
import pandas as pd
from .dataframe_builder import define_dataframe_structure, simulate_data

def separate_clusters(column_specs, n_points=100, separation=10, col_specs=None, random_state=None):
    """
    Creates cluster groups that are well-seperated from each other based on a choosed seperation factor.
    Also uses define_dataframe_structure() and simulate_data() functions from this package.

    Parameters:
        column_specs (list of dict): A list of dictionaries where each dictionary defines a column.
            Each dictionary must contain:
                - 'name' (str): Name of the column.
                - 'reps' (list): Representative points for the column.
        n_points (int): Number of data points to generate per group.
        separation (float): The factor by which to separate groups.
        col_specs (dict, optional): Column-specific simulation specifications.
            Example:
            {
                'height': {'distribution': 'normal', 'variance': 5},
                'weight': {'distribution': 'uniform', 'variance': 10}
            }
        random_state (int, optional): Random seed for reproducibility.

    Returns:
        simulated_data(pd.DataFrame): output DataFrame containing the simulated data points with well-separated groups
                                based on given seperation factor.
    """
    try:
        # Adjust representatives for separation
        adjusted_column_specs = []
        for col in column_specs:
            if 'reps' not in col or not isinstance(col['reps'], list):
                raise ValueError(f"Each column specification must include a 'reps' key with a list of representatives.")
            
            
            # Scale the representative points by separation factor to push them further apart
            adjusted_reps = [rep * separation for rep in col['reps']]
            adjusted_column_specs.append({'name': col['name'], 'reps': adjusted_reps})

        # Generate the structured DataFrame using adjusted reps
        structured_data = define_dataframe_structure(adjusted_column_specs)
        if structured_data is None:
            raise ValueError("Failed to create seed DataFrame.")

        # Generate simulated data using structured data
        simulated_data = simulate_data(structured_data, n_points=n_points, col_specs=col_specs, random_state=random_state)
        if simulated_data is None:
            raise ValueError("Failed to generate simulated data.")

        return simulated_data

    except Exception as e:
        print(f"Error in create_separated_clusters: {e}")
        return None
