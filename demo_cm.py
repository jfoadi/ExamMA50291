import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from cluster_maker import define_dataframe_structure, simulate_data

def visualize_clusters(data):
    """
    Visualizes clustered data using a scatter plot.

    This function creates a scatter plot to visualize the relationship 
    between height and weight for different groups in the provided 
    clustered data. Each group is represented by a different color.

    Parameters:
    ----------
    data : DataFrame
        A pandas DataFrame containing the clustered data. 
    Returns:
        This function displays the scatter 
        plot directly.
    """
    
    # Set the style for seaborn
    sns.set(style="whitegrid")

    # Create a scatter plot for the clustered data
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=data, x="height", y="weight", hue="group", palette="deep", s=100, alpha=0.9)

    # Add titles and labels
    plt.title("Cluster Visualization: Height vs Weight", fontsize=16)
    plt.xlabel("Height (cm)", fontsize=14)
    plt.ylabel("Weight (kg)", fontsize=14)
    plt.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    # Define column specifications for the DataFrame
    column_specs = [
        {"name": "height", "reps": [180, 160, 120, 100, 80, 150, 170]},
        {"name": "weight", "reps": [70, 60, 50, 45, 40, 80, 90]},
        {"name": "age", "reps": [20, 35, 30, 10, 24, 43, 56]},
    ]

    # Create the seed DataFrame
    seed_df = define_dataframe_structure(column_specs)

    # Define simulation specifications
    col_specs = {
        'height': {'distribution': 'normal', 'variance': 10},
        'weight': {'distribution': 'normal', 'variance': 5},
        'age': {'distribution': 'normal', 'variance': 2},
    }

    # Simulate data based on the seed DataFrame
    simulated_data = simulate_data(seed_df, n_points=100, col_specs=col_specs, random_state=42)

    # Visualize the simulated data
    visualize_data(simulated_data)

if __name__ == "__main__":
    main()