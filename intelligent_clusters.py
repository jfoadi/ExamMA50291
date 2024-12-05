import cluster_maker as cm
import pandas as pd
import numpy as np

def create_intelligent_clusters(centroids, separation, n=20, random_state=None):

    """
    Simulate clusters of data with separation between them

    Parameters:
        centroids (pd.DataFrame): DataFrame containing the centre of each cluster
        separation (int/list): Amount of separation between clusters. Can be given on a per attribute basis
        n (int, optional): Number of points to generate per cluster.
        random_state (int, optional): Random seed for reproducibility.

    Returns:
        pd.DataFrame: Simulated clustered data

    """
    
    #Check inputs are valid
    if not isinstance(centroids, pd.DataFrame):
        raise TypeError("centroids must be a pandas DataFrame")
    if not isinstance(separation, int):
        if not (isinstance(separation, list) and len(separation) == len(centroids.shape[0])):
            raise TypeError("separation must either be an integer, or a list of as many integers as centroids has rows")
        for s in separation:
            if not isinstance(s, int):
                 raise TypeError("separation must either be an integer, or a list of as many integers as centroids has rows")
    
    col_specs = {}
    for index, data in centroids.T.iterrows():
        min_dist = np.inf

        #Calculate variance required for correct spacing
        for i in range(len(data)):
            print(data)
            data = np.array(data)
            rem = np.delete(data, i)
            del rem[i]
            if isinstance(separation, int):
                dist = min(abs(rem - data[i])) - separation
            else:
                dist = min(abs(rem - data[i])) - separation[i]
            if dist <= 0:
                print(rem - data[i])
                print(dist)
                raise ValueError("Centroids must have sufficient distance between them")
            if dist < min_dist:
                min_dist = dist

        #Update the dictionary to be sent to simulate_data
        col_specs.update({index:{'distribution':'uniform', 'variance':min_dist}})
    
    intelligent_clusters = cm.simulate_data(centroids, n, col_specs, random_state)
            
