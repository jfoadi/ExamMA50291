import numpy as np
from sklearn.cluster import (KMeans,
                             AffinityPropagation,
                             MeanShift,
                             SpectralClustering,
                             AgglomerativeClustering,
                             DBSCAN,
                             OPTICS,
                             Birch)

from sklearn.mixture import GaussianMixture


def kmeans_clustering(data):
    """
    Perform K-Means clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        n_clusters = int(input("Enter the number of clusters: ").strip())
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(data)
        return kmeans.labels_
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

def affinity_propagation_clustering(data):
    """
    Perform Affinity Propagation clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        clustering = AffinityPropagation(random_state=42)
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def mean_shift_clustering(data):
    """
    Perform Mean-Shift clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        clustering = MeanShift()
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def spectral_clustering(data):
    """
    Perform Spectral Clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        n_clusters (int): Number of clusters.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        n_clusters = int(input("Enter the number of clusters: ").strip())
        clustering = SpectralClustering(n_clusters=n_clusters, random_state=42)
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def ward_hierarchical_clustering(data):
    """
    Perform Ward Hierarchical Clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        n_clusters (int): Number of clusters.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        n_clusters = int(input("Enter the number of clusters: ").strip())
        clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def agglomerative_clustering(data, linkage='ward'):
    """
    Perform Agglomerative Clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        n_clusters (int): Number of clusters.
        linkage (str): Linkage criterion ('ward', 'complete', 'average', 'single').
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        n_clusters = int(input("Enter the number of clusters: ").strip())
        clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def dbscan_clustering(data):
    """
    Perform DBSCAN clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        eps (float): The maximum distance between two samples.
        min_samples (int): Minimum number of samples for a cluster.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        min_samples = int(input("Enter the minimum samples for a cluster: ").strip())
        eps = float(input("Enter the epsilon value (eps): ").strip())
        clustering = DBSCAN(eps=eps, min_samples=min_samples)
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def optics_clustering(data):
    """
    Perform OPTICS clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        min_samples (int): Minimum number of samples for a cluster.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        min_samples = int(input("Enter the minimum samples for a cluster: ").strip())
        clustering = OPTICS(min_samples=min_samples)
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")

def gaussian_mixture_clustering(data):
    """
    Perform Gaussian Mixture Model clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        n_components (int): Number of mixture components (clusters).
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        n_components = int(input("Enter the number of mixture components: ").strip())
        gmm = GaussianMixture(n_components=n_components, random_state=42)
        gmm.fit(data)
        return gmm.predict(data)
    except Exception as e:
        print(f"An error occurred: {e}")

def birch_clustering(data):
    """
    Perform Birch clustering on the given data.
    Parameters:
        data (array-like): Data to be clustered.
        n_clusters (int): Number of clusters.
    Returns:
        labels (array): Cluster labels for each point.
    """
    try:
        n_clusters = int(input("Enter the number of clusters: ").strip())
        clustering = Birch(n_clusters=n_clusters)
        clustering.fit(data)
        return clustering.labels_
    except Exception as e:
        print(f"An error occurred: {e}")