import matplotlib.pyplot as plt
import pandas as pd

def plot_clusters(data, x='X', y='Y', cluster_col='Cluster', title='Cluster Plot', save_file=None):
    plt.figure(figsize=(8,6))
    clusters = data['Cluster'].unique()
    for cluster in clusters:
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data['X'], cluster_data['Y'], label=f'Cluster {cluster}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    if save_file:
        plt.savefig(save_file, format='png')
        print(f"Plot saved as {save_file}")
    else:
        plt.show()