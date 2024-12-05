###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module dataframe_builder.py
###

## Library needed
try:
    import numpy as np
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Numpy installed. Please install it to use this code ***")
try:
    import pandas as pd
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Pandas installed. Please install it to use this code ***")

## Function to define the object to hold the groups centers
def define_dataframe_structure(column_specs):
    """
    Create a numerical DataFrame structure based on user-defined specifications.

    Parameters:
        column_specs (list of dict): A list where each dictionary defines a numerical column.
            Each dictionary should contain:
                - 'name' (str): Name of the column.
                - 'reps' (list or range): Representative points for the column.

    Returns:
        pd.DataFrame: DataFrame with specified structure.
    """
    try:
        if not isinstance(column_specs, list):
            raise TypeError("column_specs must be a list of dictionaries")
        
        for spec in column_specs:
            if not isinstance(spec, dict):
                raise TypeError("Each item in column_specs must be a dictionary")
            if 'name' not in spec or not isinstance(spec['name'], str):
                raise ValueError("Each dictionary in column_specs must have a 'name' key with a string value")
            if 'reps' in spec and not isinstance(spec['reps'], list):
                raise TypeError("The 'reps' key in each dictionary must be a list if present")

        # Prepare data dictionary
        data = {}
        max_length = 0

        # Find the maximum length of representative points
        for spec in column_specs:
            max_length = max(max_length, len(spec.get('reps', [])))
        for spec in column_specs:
            name = spec['name']
            reps = spec.get('reps', [])
            # Extend numerical columns with NaN to match max_length
            extended_points = reps + [np.nan] * (max_length - len(reps))
            data[name] = extended_points

        # Create an empty DataFrame with specified columns and data types
        df = pd.DataFrame(data)
        return df
    except (TypeError, ValueError) as e:
        print(f"Error defining DataFrame structure: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

## Function to simulate data for all groups
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
    """
    Simulate numerical data points around seed representatives, with column-specific distributions and variances.

    Parameters:
        seed_df (pd.DataFrame): DataFrame with numerical representative points (the "seed").
        n_points (int): Number of points to generate per representative.
        col_specs (dict): Column-specific simulation specifications.
            Example:
            {
                'Age': {'distribution': 'normal', 'variance': 1.0},
                'Income': {'distribution': 'uniform', 'variance': 5000},
            }
        random_state (int, optional): Random seed for reproducibility.

    Returns:
        pd.DataFrame: DataFrame containing the simulated data points.
    """
    try:
        if not isinstance(seed_df, pd.DataFrame):
            raise TypeError("seed_df must be a pandas DataFrame")
        if seed_df.empty:
            raise ValueError("seed_df must not be an empty DataFrame")
        if not isinstance(n_points, int) or n_points <= 0:
            raise ValueError("n_points must be a positive integer")
        if col_specs is not None and not isinstance(col_specs, dict):
            raise TypeError("col_specs must be a dictionary if provided")
        if random_state is not None and not isinstance(random_state, int):
            raise TypeError("random_state must be an integer if provided")

        if random_state is not None:
            np.random.seed(random_state)
        
        simulated_data = []

        for _, representative in seed_df.iterrows():
            for _ in range(n_points):
                simulated_row = {}
                for col in seed_df.columns:
                    if col_specs and col in col_specs:
                        dist = col_specs[col].get('distribution', 'normal')
                        var = col_specs[col].get('variance', 1)
                        if dist == 'normal':
                            simulated_row[col] = np.random.normal(representative[col], var)
                        elif dist == 'uniform':
                            simulated_row[col] = np.random.uniform(representative[col] - var, representative[col] + var)
                        else:
                            raise ValueError(f"Unsupported distribution type: {dist}")
                    else:
                        simulated_row[col] = representative[col]
                simulated_data.append(simulated_row)

        return pd.DataFrame(simulated_data)
    except (TypeError, ValueError) as e:
        print(f"Error simulating data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
