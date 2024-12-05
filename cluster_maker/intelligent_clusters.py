import pandas as pd
import numpy as np
from .dataframe_builder import (
    define_dataframe_structure,
    simulate_data
)

print("Intelligent Clusters module loaded successfully.")

def create_separated_clusters(seed_df=None, column_specs=None, n_points=100, col_specs=None, separation_factor=10, random_state=None):
    """
    Generates well-separated groups of simulated data based on the separation factor.

    This function either uses an existing `seed_df` or generates one using `column_specs` to create clusters. The groups are separated by a specified `separation_factor`, and the separation is deterministic, ensuring precise control over the distance between group centers. A higher `separation_factor` results in more distinct separation between the groups.

    Parameters:
        seed_df (pd.DataFrame, optional): The seed DataFrame with the representative points for each group. If not provided, `column_specs` must be used.
        column_specs (list of dict, optional): If `seed_df` is None, this argument provides the specifications to create the seed DataFrame. Each dictionary should contain the column name and representative values.
        n_points (int): Number of data points to simulate per group (default is 100).
        col_specs (dict): Column-specific simulation specifications, such as distribution types and variance. For example:
            {
                'height': {'distribution': 'normal', 'variance': 5},
                'weight': {'distribution': 'uniform', 'variance': 10}
            }
        separation_factor (float): Controls how far apart the groups are. A higher value means greater separation (default is 10).
        random_state (int, optional): Random seed for reproducibility (default is None).

    Returns:
        pd.DataFrame: A DataFrame with the simulated data, including a 'group' column that identifies which group each point belongs to.

    """
    try:
        if seed_df is None:
            # If no seed_df is provided, generate one using column_specs
            if column_specs is None:
                raise ValueError("Either seed_df or column_specs must be provided.")
            seed_df = define_dataframe_structure(column_specs)
        
        if not isinstance(seed_df, pd.DataFrame):
            raise TypeError("seed_df must be a pandas DataFrame.")
        if seed_df.empty:
            raise ValueError("seed_df must not be empty.")
        if not isinstance(separation_factor, (int, float)) or separation_factor <= 0:
            raise ValueError("separation_factor must be a positive number.")
        
        # Create a copy of the seed DataFrame to modify the group centers
        separated_seed_df = seed_df.copy()

        # Determine the number of groups (based on seed DataFrame)
        num_groups = len(separated_seed_df)

        # Generate deterministic shifts based on separation_factor
        # This ensures that each group center is spaced exactly by separation_factor
        for i, row in separated_seed_df.iterrows():
            shift_vector = np.zeros_like(row)
            shift_vector[0] = i * separation_factor  # Only shift the first feature (e.g., height) for separation
            separated_seed_df.iloc[i] += shift_vector

        # Simulate data around the new, well-separated centers
        simulated_data = simulate_data(separated_seed_df, n_points=n_points, col_specs=col_specs, random_state=random_state)

        # Add a group label for identification
        simulated_data['group'] = np.repeat(range(num_groups), n_points)

        return simulated_data

    except (TypeError, ValueError) as e:
        print(f"Error creating separated clusters: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
