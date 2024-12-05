import matplotlib.pyplot as plt
import pandas as pd

def plot_clusters(data, x='X', y='Y', cluster_col='Cluster', title='Cluster Plot'):
    plt.figure(figsize=(8,6))
    clusters = data['Cluster'].unique()
    for cluster in clusters:
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data['X'], cluster_data['Y'], label=f'Cluster {cluster}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simulated Data from cluster_maker')
    plt.legend()
    plt.show()