
print("""This code is a demostration of the use of the package cluster_maker and intelligent cluster function. It creates to the structure of a DataFrame and simulate data based on the defined structure.
         It then exports the simulated data to a CSV file in the ouputs directory.""")

# Basic libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## Import cluster_maker
import cluster_maker as cm
# Import sklearn libraries
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN



print("----------------------------------------------------------------------------")
print("--------------------------Use of cluster_maker package----------------------")
print("----------------------------------------------------------------------------")


print("----------------------------------------------------------------------------")
print("----------------------------First step-------------------------------------")
print("----------------------------------------------------------------------------")

print("1st step: Creating the structure of the DataFrame")
print("Input: column_specs is the column specifications. It is a list of dictionaries. It should look like this:")
column_specs = [
    {'name': 'height', 'reps': [180, 160, 120]},
    {'name': 'weight', 'reps': [80, 60, 30]},
    {'name': 'age', 'reps': [40, 35, 10]}
]
print(column_specs) 

print("Ouput: Creating the DataFrame structure:")
df = cm.define_dataframe_structure(column_specs)
print("""The DataFrame structure has three variables: \n
      - height,
      - weight and 
      - age \n
      Each variable has representative values""")
print("The code is: cm.define_dataframe_structure(column_specs)" )
print("The output is:")
print(df)

print("----------------------------------------------------------------------------")
print("----------------------------Second step-------------------------------------")
print("----------------------------------------------------------------------------")
print("2nd step: Simulate data based on the defined structure")

print("Input: seed_df is the DataFrame structure created in the first step. This looks like this:")
print(df)
print("Input: n_points is the number of data points to simulate for each representative point.")
n_points = 20
print("np_points = ", n_points)

print("Input: col_specs is the column specifications. It is a dictionary. It should look like this:")
col_specs = {'height':{'distibution':'normal','variance':0.1},
            'weight':{'distribution':'uniform','variance':0.2},
            'age':{'distribution':'normal','variance':0.3}}
print(col_specs)
print("Input: random_state is the random seed for reproducibility.")
random_state = 42
print("random_state = ", random_state)

print("Output: The code for simulating data is cm.simulate_data(df, n_points, col_specs, random_state)")
print("Output: Simulating data based on the defined structure:")
data = cm.simulate_data(df, n_points, col_specs, random_state)
print("The simulated data statistics looks like this:")
print(cm.calculate_descriptive_statistics(data))
print("The correlation matrix of the simulated data is:")
print(cm.calculate_correlation(data))

print("----------------------------------------------------------------------------")
print("----------------------------Third step--------------------------------------")
print("----------------------------------------------------------------------------")
print("3rd step: Exporting the simulated data to a CSV file in the data directory")
print("The code for exporting the data is cm.export_to_csv(data, 'outputs/simulated_data.csv')")
cm.export_to_csv(data, 'outputs/simulated_data.csv')
print("The data has been exported to the file outputs/simulated_data.csv")

print("-----------------------------------------------------------------------")
print("Exports the DataFrame to a text file with formatted numbers.")
print("The code for exporting the data is cm.export_formatted(data, 'outputs/formatted_data.txt')")
cm.export_formatted(data, 'outputs/formatted_data.txt')


print("----------------------------------------------------------------------------")
print("----------------------------Fourth step--------------------------------------")
print("----------------------------------------------------------------------------")
print("4th step: Intelligent clustering of the simulated data")
print("Input: data is the simulated data. This looks like this:")
print(data.head())
print("Input: cluster_separation is the number of clusters to create.")
cluster_separation = 3
print("cluster_separation = ", cluster_separation)
print("Input: clustering_method is the clustering method to use. It should be one of 'kmeans', 'agglomerative', or 'dbscan'.")
clustering_method = 'kmeans'
print("clustering_method = ", clustering_method)
print("Output: The code for intelligent clustering is cm.intelligent_clustering(data, cluster_separation, clustering_method)")
print("Output: Intelligent clustering of the simulated data:")
df_cluster = cm.intelligent_clustering(data, cluster_separation, clustering_method)
print("The intelligent clustering of the simulated data looks like this:")
print(df_cluster.head())
print("Output: The code for calculating cluster statistics is cm.calculate_cluster_stats(df_cluster)")
print("Output: Calculating cluster statistics:")
cluster_stats = cm.calculate_cluster_stats(df_cluster)
print("The cluster statistics are:")
print(cluster_stats)

print("----------------------------------------------------------------------------")
print("----------------------------Fifth step--------------------------------------")
print("----------------------------------------------------------------------------")
print("5th step: Export the intelligent clustering data to a CSV file in the outputs directory")
print("The code for exporting the data is cm.export_to_csv(df_cluster, 'outputs/intelligent_clustered_data.csv')")
cm.export_to_csv(df_cluster, 'outputs/intelligent_clustered_data.csv')
print("The intelligent clustering data has been exported to the file outputs/intelligent_clustered_data.csv")







