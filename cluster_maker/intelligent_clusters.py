
# Intelligent Clustering module

# importing relevant libraries 

import pandas as pd
import numpy as np
from .dataframe_builder import simulate_data

# Function to create a cluster of data points: 

def create_intelligent_clusters(seed_df, n_points = 100, separation = 10, random_state = None): 
    """
    Function: Create well-separated groups based on the seed DataFrame and using simulate_data().

    Parameters:
        seed_df (pd.DataFrame): DataFrame with numerical representative points (the "seed").
        n_points (int): Number of points to generate per representative.
        separation (float): Distance to separate the groups.
        random_state (int, optional): Random seed for reproducibility.

    Returns:
        pd.DataFrame: DataFrame containing the simulated data points with well-separated groups.
    """

    # Exception handling of the input parameters
    try: 
        if not isinstance(seed_df, pd.DataFrame): 
            raise TypeError("seed_df must be a pandas DataFrame")
        if seed_df.empty: 
            raise ValueError("seed_df must not be an empty DataFrame")
        if not isinstance(n_points, int) or n_points <= 0: 
            raise ValueError("n_points must be a positive integer")
        if not isinstance(separation, (int, float)) or separation <= 0: 
            raise ValueError("Separation must be a positive integer or float")
        if random_state is not None and not isinstance(random_state, int): 
            raise TypeError("random_state must be an integer if provided")
        
        if random_state is not None: 
            np.random.seed(random_state)

        # implementing adjusted seed DataFrame to ensure separation between groups
        adjusted_seed_df = seed_df.copy()
        for i, col in enumerate(adjusted_seed_df.columns): 
            adjusted_seed_df[col] += i * separation

        # Using simulate_data function to generate data points
        simulated_data = simulate_data(adjusted_seed_df, n_points, random_state = random_state)

        return simulated_data
    
    except (TypeError, ValueError) as e: 
        print(f'Error creating intelligent clusters: {e}')
        return None
    except Exception as e: 
        print(f'And unexpected error occured: {e}')
        return None
    
    


