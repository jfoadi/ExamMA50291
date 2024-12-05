import pandas as pd
import numpy as np
import cluster_maker.dataframe_builder as dfb
from sklearn.cluster import KMeans

def intelligent_cluster(df, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters)# Create a KMeans object
    kmeans.fit(df)
    df['group'] = kmeans.labels_ # Create a new column 'group' with the cluster to which each row belongs
    return df

if __name__ == '__main__':
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    
    df = dfb.define_dataframe_structure(column_specs)
    print(df)
    data = dfb.simulate_data(df, 20)

    clustered_data = intelligent_cluster(data)
    print(clustered_data)




   












