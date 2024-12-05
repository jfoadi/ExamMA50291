
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import cluster_maker as cm
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

# Intelliogent cluster function

def intelligent_clustering(data, cluster_separation, clustering_method):
    """
    Run the specified clustering method on the given data and print the cluster labels assigned by the model.

    Args:
    data (array-like): The data to be clustered.
    cluster_separation (int): The number of clusters to create.
    clustering_method: The clustering method to use. One of 'kmeans', 'agglomerative', or 'dbscan'.

    Returns:
    dataframe: The data frame contains the simulated data and a column named intelligent_cluster with cluster labels
    """
    try:
        # Import the required clustering model
        df_cluster = data.copy()
        # Create an instance of the specified clustering model
        if clustering_method == 'kmeans':
            model = KMeans(n_clusters=cluster_separation)
        elif clustering_method == 'agglomerative':
            model = AgglomerativeClustering(n_clusters=cluster_separation)
        elif clustering_method == 'dbscan':
            model = DBSCAN(eps=0.5, min_samples=5)
        else:
            raise ValueError("Invalid clustering method specified.")

        # Fit the clustering model to the data
        model.fit(data)

        # Get the cluster labels assigned by the model
        labels = model.labels_

        df_cluster['intelligent_cluster'] = labels

        # Return the cluster data frame
        return df_cluster
    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Calculate cluster statistics

def calculate_cluster_stats(df):
    """
    Calculate descriptive statistics for each cluster in the given DataFrame.

    Args:
    df (pandas.DataFrame): The DataFrame containing the cluster labels.

    Returns:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for each cluster.
    """
    
    try:
        cluster_stats = df.groupby('intelligent_cluster')
        
        for column in df.columns[:-1]:
            stats = cluster_stats[column].describe()
            print(f"Descriptive statistics for {column}:")
            print(stats)
            print()
        
        return cluster_stats
    except Exception as e:
        print("An error occurred:", str(e))
        return None
