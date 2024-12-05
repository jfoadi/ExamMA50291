###
## cluster_maker
## A package to simulate clusters of data points.
## Adam Young - University of Bath - 2024
##
## Module intelligent_clusters.py
###


## Import necessary libraries, give a relevent error message if they are not installed correctly.
try:
    import numpy as np
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Numpy installed. Please install it to use this code ***")
try:
    import pandas as pd
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Pandas installed. Please install it to use this code ***")

import cluster_maker as cm

def create_separated_clusters(seed_df, n_points=100, col_specs=None, random_state=666, group_separation=10):
    """
    Create well-separated clusters based on the seed DataFrame and simulate data points with group separation.

    Parameters:
        seed_df (pd.DataFrame): The DataFrame with representative points for each group.
        n_points (int): Number of points to generate per group (default: 100).
        col_specs (dict): Column-specific simulation specifications (default: None).
        random_state (int): Random seed for reproducibility (default: None).
        group_separation (float): The distance between each group (default: 10).
        
    Returns:
        final_data: A DataFrame containing the simulated, well-separated clusters.
    """
    try:
        # CHECK 1: Check to see if the data is a Pandas DataFrame
        if not isinstance(seed_df, pd.DataFrame):
            raise TypeError("\n*** ERROR: The input data must be a pandas DataFrame. ***")
        
        # CHECK 2: Check to see if the n_points is a positive integer
        if not isinstance(n_points, int) or n_points <= 0:
            raise ValueError("\n*** ERROR: n_points must be a positive integer. ***")

        # CHECK 3: Check to see if the group_separation is a positive number
        if not isinstance(group_separation, (int, float)) or group_separation <= 0:
            raise ValueError("\n*** ERROR: group_separation must be a positive number. ***")

        # Set random state for reproducibility
        if random_state is not None:
            np.random.seed(random_state)

        # Prepare a list to collect the simulated data
        simulated_data = []

        # Generate clusters with separation
        for idx, representative in seed_df.iterrows():
            # Create a separation factor for each group based on the index
            separation_offset = idx * group_separation
            
            # Adjust the representative point by adding separation offset
            adjusted_reps = representative + separation_offset
            
            # Simulate data for this group using the adjusted representatives
            group_data = cm.simulate_data(pd.DataFrame([adjusted_reps]), n_points=n_points, col_specs=col_specs, random_state=random_state)
            
            # Append the simulated data to the list
            simulated_data.append(group_data)

        # Concatenate all groups to create the final DataFrame
        final_data = pd.concat(simulated_data, ignore_index=True)
        
        return final_data
    
    except (TypeError, ValueError) as e:
        print(f"\n*** ERROR: creating separated clusters: {e} ***")
        return None
    except Exception as e:
        print(f"\n*** ERROR: An unexpected error occurred: {e} ***")
        return None
