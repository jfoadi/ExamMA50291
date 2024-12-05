# Library needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cluster_maker.dataframe_builder import simulate_data
from sklearn.datasets import make_blobs

# Function to create well-seperated clusters of data points
def create_clusters(seed_df, n_points, col_specs=None, random_state=None, group_separation=5.0):
    """
    Create clusters (well-separated groups) of data points based on a seed DataFrame.

    Parameters:
        seed_df (pd.DataFrame): Seed DataFrame with group centers.
        n_points (int): Number of data points to simulate per group.
        col_specs (dict): Dictionary with column specifications for data simulation.
        random_state (int): Random seed for reproducibility.
        group_separation (float): Separation factor for groups.

    Returns:
        pd.DataFrame: DataFrame with simulated clusters.
    """
    try:
        if not isinstance(seed_df, pd.DataFrame):
            raise TypeError("seed_df must be a pandas DataFrame")
        if not isinstance(n_points, int) or n_points <= 0:
            raise ValueError("n_points must be a positive integer")
        if not isinstance(col_specs, dict):
            raise TypeError("col_specs must be a dictionary")
        if not all(isinstance(v, dict) for v in col_specs.values()):
            raise ValueError("Values in col_specs must be dictionaries")
        if not isinstance(group_separation, (int, float)) or group_separation <= 0:
            raise ValueError("separation must be a positive number")
        if not all('distribution' in v and 'variance' in v for v in col_specs.values()):
            raise ValueError("Each dictionary in col_specs must have 'distribution' and 'variance' keys")

        # Generate well-separated cluster centers using make_blobs (integrates seperation as std)
        cluster_centers = seed_df.values
        X, labels = make_blobs(
            n_samples=len(cluster_centers),
            centers=cluster_centers,
            cluster_std=group_separation,
            random_state=random_state
        )

        # Create temporary DataFrame for the generated centers
        temp_centers_df = pd.DataFrame(X, columns=seed_df.columns)

        simulated_data = []
        for i, center in temp_centers_df.iterrows():
            # Select rows corresponding to the same cluster
            cluster_seed_df = pd.DataFrame([center], columns=seed_df.columns)
            
            # Use simulate_data to generate data points around these centers
            cluster_data = simulate_data(seed_df=cluster_seed_df, n_points=n_points, col_specs=col_specs, random_state=random_state)
            cluster_data['Cluster'] = labels[i]
            simulated_data.append(cluster_data)

        # Concatenate all cluster data into a single DataFrame
        final_data = pd.concat(simulated_data, ignore_index=True)
        return final_data

    except Exception as e:
        raise RuntimeError(f"Error in create_clusters: {str(e)}")
    
# Function to plot clusters defined above
def plot_clusters(clusters, x_col=None, y_col=None, cluster_col='Cluster', title="Cluster Visualization"):
    """
    Parameters:
        clusters (pd.DataFrame): DataFrame containing the cluster data.
        x_col (str): Column name for the x-axis. Default is the first numeric column.
        y_col (str): Column name for the y-axis. Default is the second numeric column.
        cluster_col (str): Column name representing cluster labels. Default is 'Cluster'.
        title (str): Title of the plot. Default is 'Cluster Visualization'.
    """
    try:
        if not isinstance(clusters, pd.DataFrame):
            raise TypeError("The clusters parameter must be a pandas DataFrame")
        if cluster_col not in clusters.columns:
            raise ValueError(f"Cluster column '{cluster_col}' must exist in the DataFrame")

        # Automatically detect x_col and y_col if not provided
        if x_col is None or y_col is None:
            numeric_cols = clusters.select_dtypes(include=[np.number]).columns
            x_col = x_col or numeric_cols[0]
            y_col = y_col or numeric_cols[1]

        # Show scatter plot with different colors for each cluster
        plt.figure(figsize=(10, 8))
        for cluster in clusters[cluster_col].unique():
            cluster_data = clusters[clusters[cluster_col] == cluster]
            plt.scatter(
                cluster_data[x_col],
                cluster_data[y_col],
                label=f'Cluster {cluster}',
                alpha=0.7
            )
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error in plot_clusters: {e}")
