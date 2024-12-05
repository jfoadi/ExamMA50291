## 7) Add a new function to a new module called 
## "intelligent_clusters.py" that, based on the seed dataframe
## created by define_dataframe_structure(), and using simulate_data(),
## creates groups which are well separated from each other. Among
## the input parameters, make sure to include one that describes group
## separation.

from .dataframe_builder import simulate_data
import pandas as pd
import numpy as np

## Function to create well-separated groups based on seed data frame
def sepatared_groups(data, separation=3, col_specs=None, n_groups = 3, n_points = 100, random_state=None):
    """
    Create well-separated groups based on the seed data frame.
    
    Parameters:
        data (pd.DataFrame): The seed data frame.
        separation (float): The separation between groups.
        col_specs (dict): A dictionary specifying the distribution and variance for each column.
        n_groups (int): The number of groups to create.
        n_points (int): The number of points to simulate for each group.
        random_state (int): Random state for reproducibility.
    
    Returns:
        pd.DataFrame: Data frame with well-separated groups.
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        if not isinstance(separation, (int, float)):
            raise TypeError("separation must be a number")
        if col_specs is not None and not isinstance(col_specs, dict):
            raise TypeError("col_specs must be a dictionary if provided")
        if separation <= 0:
            raise ValueError("separation must be greater than 0")
        if not isinstance(n_groups, int) or n_groups < 2:
            raise ValueError("n_groups must be an integer greater than 1")
        
        # Initialize an empty list to store the groups
        all_groups = []

        # Create separated groups
        for i in range(n_groups):
            new_data = {}

            for col in data.columns:
                # Calculate the mean and standard deviation of the column
                col_mean = data[col].mean()
                col_std = data[col].std()

                random_component = np.random.uniform(-separation / 2, separation / 2) / (i+1)

                addition = (i - n_groups // 2) * separation * col_std

                new_data[col] = (col_mean + addition + random_component)*random_component

                print(new_data[col])

            new_df = pd.DataFrame(new_data, index=[0])

            simulated_df = simulate_data(new_df, n_points=n_points, col_specs=col_specs, random_state=random_state)

            all_groups.append(simulated_df)

        final_df = pd.concat(all_groups, ignore_index=True)

        return final_df
    
    except Exception as e:
        print(f"Error creating separated groups: {e}")
        return None