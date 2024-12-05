import pandas as pd
import matplotlib.pyplot as plt
from cluster_maker import (define_dataframe_structure, create_separated_clusters)


if __name__ == '__main__':
    # Create input for define_dataframe_structure with more interesting data
    column_specs = [
        {'name': 'height', 'reps': [150, 160, 170, 180, 190]},
        {'name': 'weight', 'reps': [50, 60, 70, 80, 90]},
        {'name': 'age', 'reps': [20, 30, 40, 50, 60]},
        {'name': 'income', 'reps': [30000, 40000, 50000, 60000, 70000]}
    ]
    
    # Create the seed dataframe based on the above info
    seed_df = define_dataframe_structure(column_specs)
    print("Seed DataFrame:")
    print(seed_df)

    # Define column specifications for simulation
    col_specs_simulate = {
        'height': {'distribution': 'normal', 'variance': 5},
        'weight': {'distribution': 'normal', 'variance': 10},
        'age': {'distribution': 'normal', 'variance': 5},
        'income': {'distribution': 'uniform', 'variance': 10000}
    }

    # Create well-separated clusters
    simulated_data = create_separated_clusters(seed_df, points=100, col_specs=col_specs_simulate, separation=200, random_state=42)
    print("\nSimulated Data with Separated Clusters:")
    print(simulated_data)

    # Add a cluster label to the simulated data based on the original representative points
    cluster_labels = []
    for i in range(len(seed_df)):
        cluster_labels.extend([i] * 100)
    
    # Ensure the length of cluster_labels matches the length of simulated_data
    print(f"Length of cluster_labels: {len(cluster_labels)}")
    print(f"Length of simulated_data: {len(simulated_data)}")

    simulated_data['cluster'] = cluster_labels[:len(simulated_data)]


    # Plotting the simulated data to show clusters
    plt.figure(figsize=(12, 10))

    # Scatter plot for height vs weight
    plt.subplot(2, 2, 1)
    for cluster in simulated_data['cluster'].unique():
        cluster_data = simulated_data[simulated_data['cluster'] == cluster]
        plt.scatter(cluster_data['height'], cluster_data['weight'], alpha=0.5, label=f'Cluster {cluster}')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.title('Height vs Weight')
    plt.legend()

    # Scatter plot for height vs age
    plt.subplot(2, 2, 2)
    for cluster in simulated_data['cluster'].unique():
        cluster_data = simulated_data[simulated_data['cluster'] == cluster]
        plt.scatter(cluster_data['height'], cluster_data['age'], alpha=0.5, label=f'Cluster {cluster}')
    plt.xlabel('Height')
    plt.ylabel('Age')
    plt.title('Height vs Age')
    plt.legend()



    # Scatter plot for height vs income
    plt.subplot(2, 2, 3)
    for cluster in simulated_data['cluster'].unique():
        cluster_data = simulated_data[simulated_data['cluster'] == cluster]
        plt.scatter(cluster_data['height'], cluster_data['income'], alpha=0.5, label=f'Cluster {cluster}')
    plt.xlabel('Height')
    plt.ylabel('Income')
    plt.title('Height vs Income')
    plt.legend()

    # Scatter plot for weight vs income
    plt.subplot(2, 2, 4)
    for cluster in simulated_data['cluster'].unique():
        cluster_data = simulated_data[simulated_data['cluster'] == cluster]
        plt.scatter(cluster_data['weight'], cluster_data['income'], alpha=0.5, label=f'Cluster {cluster}')
    plt.xlabel('Weight')
    plt.ylabel('Income')
    plt.title('Weight vs Income')
    plt.legend()

    plt.tight_layout()
    plt.suptitle("Scatter Plots of Simulated Data with Separated Clusters", y=1.02)
    plt.savefig("intelligent_cluster_demo.png")
    plt.show()