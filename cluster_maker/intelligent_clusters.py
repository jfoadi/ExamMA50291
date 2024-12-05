import pandas as pd
import numpy as np
import  cluster_maker as cm

def create_clusters(seed_df, n_points=50, col_specs=None, separation_factor=20, n_clusters=3):
    """
    Generate the specified number of clusters with well-separated data points based on the seed DataFrame.

    Parameters:
        seed_df Dataframe: DataFrame containing seed representative points.
        n_points (int): Number of points to generate per cluster.
        col_specs (dict): Column-specific simulation specifications.
        separation_factor (float): Factor to control separation between clusters.
        n_clusters (int): Number of clusters to create.

    Returns:
        pd.DataFrame: DataFrame containing simulated cluster data.
    """
    n_clusters+=1
    try:
        if not isinstance(seed_df, pd.DataFrame):
            raise TypeError("seed_df must be a pandas DataFrame")
        if seed_df.empty:
            raise ValueError("seed_df must not be an empty DataFrame")
        if not isinstance(n_points, int) or n_points <= 0:
            raise ValueError("n_points must be a positive integer")
        if col_specs is not None and not isinstance(col_specs, dict):
            raise TypeError("col_specs must be a dictionary if provided")

        if n_clusters > len(seed_df):
            raise ValueError("n_clusters cannot exceed the number of seed representatives")

        selected_seeds = seed_df.sample(n_clusters, random_state=42).reset_index(drop=True)  # Ensure n_clusters
        simulated_data = []

        for idx in range(n_clusters):  # Iterate through the number of clusters
            representative = selected_seeds.iloc[idx]
            for _ in range(n_points):
                simulated_row = {}
                for col in seed_df.columns:
                    if col_specs and col in col_specs:
                        dist = col_specs[col].get('distribution', 'normal')
                        var = col_specs[col].get('variance', 1)
                        if dist == 'normal':
                            simulated_row[col] = np.random.normal(
                                representative[col] + idx * separation_factor, var
                            )
                        elif dist == 'uniform':
                            simulated_row[col] = np.random.uniform(
                                representative[col] - var + idx * separation_factor,
                                representative[col] + var + idx * separation_factor
                            )
                        else:
                            raise ValueError(f"Unsupported distribution type: {dist}")
                    else:
                        simulated_row[col] = representative[col] + idx * separation_factor
                simulated_data.append(simulated_row)

        return pd.DataFrame(simulated_data)
    except (TypeError, ValueError) as e:
        print(f"Error creating separated clusters: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
