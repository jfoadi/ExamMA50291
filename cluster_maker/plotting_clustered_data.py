# plotting_clustered_data.py

import matplotlib.pyplot as plt

# function to plot the clustered data



def plot_clustering_data(data, labels, title="Clustered Data"):
    """
    Plot the clustered data points with different colors for each cluster.
    
    Parameters:
    - data (DataFrame): The input data points.
    - labels (array): The cluster labels assigned to each data point.
    - title (str): The title of the plot.
    """
    try:
        plt.figure(figsize=(8, 6))
        plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6)
        plt.title(title)
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.colorbar(label='Cluster')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting the data: {e}")


