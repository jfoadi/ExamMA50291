import pandas as pd
import numpy as np
from .dataframe_builder import define_dataframe_structure, simulate_data
from .plot_clusters import plot_clusters
from .data_exporter import export_formatted, export_to_csv 

def intelligent_cluster_groups(column_specs, n_points=100, col_specs=None, group_separation_factor=1.0, random_state=42):
    
    seed_df = define_dataframe_structure(column_specs) # creates seed dataframe showing the cluster centres
    
    # changes the cluster centres to be well separated.
    for i in seed_df.columns:
        col_mean = np.mean(seed_df[i]) # This calculates the mean of the inputted dataframe points
        seed_df[i] = col_mean + (seed_df[i] - col_mean) * group_separation_factor # by computing the difference between each value and the mean, multiplying by the separation factor creates well separated data points if separaion factor > 1.
    
    # This simulates data points around the changed cluster centres 
    data = simulate_data(seed_df, n_points=n_points, col_specs=col_specs, random_state=42)
    
    # Assign cluster labels based on the new cluster centre points
    number_of_clusters = len(seed_df)
    cluster_labels = []
    for cluster_number in range(number_of_clusters):
        cluster_labels.extend([cluster_number] * n_points)
    data['Cluster'] = cluster_labels

    plot_clusters(data, seed_df, title='Cluster Groups with a separation factor of '+ str(group_separation_factor), save_file='cluster_groups_separation_factor_'+str(group_separation_factor)+'.png')
    export_formatted(data, 'clusters_separation_factor_'+str(group_separation_factor)+'.txt', include_index=True)
    export_to_csv(data, 'clusters_separation_factor_'+str(group_separation_factor)+'.csv', delimiter=",", include_index=True)
    
    return data
