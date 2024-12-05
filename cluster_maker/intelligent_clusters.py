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
        separation (int/float): The separation between groups (closer to 1 means groups are closer together).
        col_specs (dict): A dictionary specifying the distribution and variance for each column.
        n_groups (int): The number of groups to create.
        n_points (int): The number of points to simulate for each group.
        random_state (int): Random state for reproducibility.
    
    Returns:
        pd.DataFrame: Data frame with well-separated groups.
    """
    try:
        # Exception handling
        # Check if the input is a DataFrame
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        # Check if separation is a number
        if not isinstance(separation, (int, float)):
            raise TypeError("separation must be a number")
        # Check if separation is greater than or equal to 1
        if separation < 1:
            raise ValueError("separation must be greater than 0")
        # Check if n_groups is an integer greater than 1 (we want multiple groups)
        if not isinstance(n_groups, int) or n_groups < 2:
            raise ValueError("n_groups must be an integer greater than 1")
        # Check if n_points is a positive integer        
        if not isinstance(n_points, int) or n_points <= 0:
            raise ValueError("n_points must be a positive integer")
        # Check if col_specs is a dictionary if provided
        if col_specs is not None and not isinstance(col_specs, dict):
            raise TypeError("col_specs must be a dictionary if provided")
        # Check if random_state is an integer if provided
        if random_state is not None and not isinstance(random_state, int):
            raise TypeError("random_state must be an integer if provided")
        
        # Set random seed if provided
        if random_state is not None:
            np.random.seed(random_state)


        # Initialize an empty list to store the groups
        all_groups = []

        # Create separated groups
        for i in range(n_groups):
            new_data = {}

            for col in data.columns:
                # Calculate the mean and standard deviation of the column
                col_mean = data[col].mean()
                col_std = data[col].std()

                # Add a random component to the column value for fun
                random_component = np.random.uniform(-separation / 2, separation / 2)

                # Calculate the addition to the mean for the separation
                # Depending on the number of groups, the separation factor, and the standard deviation
                addition = (i - n_groups // 2) * col_std * separation

                # Generate the new column value based on the mean, separation, and random component
                new_data[col] = col_mean + addition + random_component

                # Ensure the sign of the new value is consistent with the original mean
                if new_data[col]*col_mean < 0:
                    new_data[col] = -new_data[col]

            # Create a new DataFrame with the new data
            new_df = pd.DataFrame(new_data, index=[0])

            # Simulate data points around the new representative points
            # Based on input column specifications
            simulated_df = simulate_data(new_df, n_points=n_points, col_specs=col_specs, random_state=random_state)

            # Append the simulated data to the list of groups
            all_groups.append(simulated_df)

        # Concatenate all groups into a single DataFrame
        return pd.concat(all_groups, ignore_index=True)
    
    except Exception as e:
        print(f"Error creating separated groups: {e}")
        return None