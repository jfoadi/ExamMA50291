import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from cluster_maker import define_dataframe_structure, simulate_data

def visualize_data(data):
    # Set the style for seaborn
    sns.set(style="whitegrid")

    # Create a figure with a specified size
    plt.figure(figsize=(10, 15))

    # Scatter plot for Height vs Weight
    plt.subplot(3, 1, 1)
    sns.scatterplot(data=data, x="height", y="weight", color="blue", s=100)
    plt.title("Height vs Weight", fontsize=16)
    plt.xlabel("Height (cm)", fontsize=14)
    plt.ylabel("Weight (kg)", fontsize=14)
    plt.grid(True)

    # Scatter plot for Age vs Weight
    plt.subplot(3, 1, 2)
    sns.scatterplot(data=data, x="age", y="weight", color="orange", s=100)
    plt.title("Age vs Weight", fontsize=16)
    plt.xlabel("Age (years)", fontsize=14)
    plt.ylabel("Weight (kg)", fontsize=14)
    plt.grid(True)

    # Scatter plot for Height vs Age
    plt.subplot(3, 1, 3)
    sns.scatterplot(data=data, x="height", y="age", color="green", s=100)
    plt.title("Height vs Age", fontsize=16)
    plt.xlabel("Height (cm)", fontsize=14)
    plt.ylabel("Age (years)", fontsize=14)
    plt.grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.suptitle("Visualizations of Simulated Data", fontsize=20, y=1.02)

    # Show the plots
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