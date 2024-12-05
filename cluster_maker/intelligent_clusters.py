# intelligent_clusters.py

import pandas as pd
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, SpectralClustering
from sklearn.cluster import AgglomerativeClustering, DBSCAN, OPTICS, Birch
from sklearn.mixture import GaussianMixture
import numpy as np

def intelligent_clustering(df, n_clusters, separation_factor=1.0, n_points=100, algorithm="kmeans"):
    """
    Perform clustering on the given DataFrame using the specified algorithm.
    
    Parameters:
    - df (DataFrame): The input data to cluster.
    - n_clusters (int): The number of clusters to form.
    - separation_factor (float): The separation factor to control the spread of the clusters.
    - n_points (int): The number of data points to generate for clustering.
    - algorithm (str): The clustering algorithm to use (options: "kmeans", "affinity", "meanshift", "spectral", "agglo", "dbscan", "optics", "gmm", "birch").
    
    Returns:
    - clustered_data (DataFrame): DataFrame containing the original data with an added 'cluster' column indicating the assigned cluster.
    """
    
    # Simulate data points if necessary
    if df is None:
        print("❌ No DataFrame provided for clustering.")
        return None
    
    simulated_data = simulate_data(df, n_points=n_points, random_state=42)
    
    # Perform clustering based on the selected algorithm
    if algorithm == "kmeans":
        model = KMeans(n_clusters=n_clusters, random_state=42)
    elif algorithm == "affinity":
        model = AffinityPropagation(random_state=42)
    elif algorithm == "meanshift":
        model = MeanShift()
    elif algorithm == "spectral":
        model = SpectralClustering(n_clusters=n_clusters, random_state=42)
    elif algorithm == "agglo":
        model = AgglomerativeClustering(n_clusters=n_clusters)
    elif algorithm == "dbscan":
        model = DBSCAN()
    elif algorithm == "optics":
        model = OPTICS()
    elif algorithm == "gmm":
        model = GaussianMixture(n_components=n_clusters, random_state=42)
    elif algorithm == "birch":
        model = Birch(n_clusters=n_clusters)
    else:
        print(f"❌ Unknown algorithm: {algorithm}")
        return None
    
    # Fit the model and predict clusters
    try:
        cluster_labels = model.fit_predict(simulated_data)
        simulated_data['cluster'] = cluster_labels
        print(f"\nClustering completed using {algorithm} algorithm.")
        return simulated_data
    except Exception as e:
        print(f"❌ Error performing clustering with {algorithm}: {e}")
        return None


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
