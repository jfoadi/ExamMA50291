# demo_clustering.py

# this demonstrates the use of the clustering functions in the package cluster_maker
# including the following functions: kmeans_clustering, affinity_propagation_clustering, 
# mean_shift_clustering, spectral_clustering, ward_hierarchical_clustering, agglomerative_clustering, 
# dbscan_clustering, optics_clustering, gaussian_mixture_clustering, birch_clustering

# Import necessary libraries
import cluster_maker as cm
import pandas as pd
import prettytable as pt
from prettytable import PrettyTable
import sys
import numpy as np  # Make sure to import numpy

# Function to display DataFrame using PrettyTable
def display_dataframe(df, title="DataFrame"):
    table = PrettyTable(df.columns.tolist())
    for row in df.itertuples(index=False):
        table.add_row(row)
    print(f"\n{title}:\n")
    print(table)

# Import clustering functions from your custom package
try:
    from cluster_maker import (
        kmeans_clustering,
        affinity_propagation_clustering,
        mean_shift_clustering,
        spectral_clustering,
        ward_hierarchical_clustering,
        agglomerative_clustering,
        dbscan_clustering,
        optics_clustering,
        gaussian_mixture_clustering,
        birch_clustering,
        intelligent_clustering,
        calculate_correlation,
        calculate_descriptive_statistics,
        generate_custom_data,
        evaluate_clustering,
        plot_clustering_data
    )
except ImportError as e:
    print(f"Error: {e}. Please ensure that 'cluster_maker' is available and contains the required functions.")
    sys.exit(1)

# Function to display a correlation matrix using PrettyTable
def display_correlation_matrix(correlation_matrix):
    """
    Display a correlation matrix using PrettyTable.

    Parameters:
    correlation_matrix (pd.DataFrame): The correlation matrix to display.
    """
    try:
        table = PrettyTable()
        table.field_names = [""] + correlation_matrix.columns.tolist()
        for row in correlation_matrix.itertuples():
            table.add_row([row.Index] + list(row[1:]))
        print("\nCorrelation Matrix:")
        print(table)
    except Exception as e:
        print(f"Error displaying correlation matrix: {e}")

# Function to display descriptive statistics using PrettyTable
def display_descriptive_statistics(stats):
    """
    Display descriptive statistics using PrettyTable.

    Parameters:
    stats (pd.DataFrame): The descriptive statistics to display.
    """
    try:
        table = PrettyTable()
        table.field_names = ["Statistic"] + stats.columns.tolist()
        for row in stats.itertuples():
            table.add_row([row.Index] + list(row[1:]))
        print("\nDescriptive Statistics:")
        print(table)
    except Exception as e:
        print(f"Error displaying descriptive statistics: {e}")

# Dictionary linking algorithm numbers to their names and functions
clustering_algorithms = {
    "1": ("K-Means", kmeans_clustering),
    "2": ("Affinity Propagation", affinity_propagation_clustering),
    "3": ("Mean-Shift", mean_shift_clustering),
    "4": ("Spectral Clustering", spectral_clustering),
    "5": ("Ward Hierarchical Clustering", ward_hierarchical_clustering),
    "6": ("Agglomerative Clustering", agglomerative_clustering),
    "7": ("DBSCAN", dbscan_clustering),
    "8": ("OPTICS", optics_clustering),
    "9": ("Gaussian Mixtures", gaussian_mixture_clustering),
    "10": ("Birch", birch_clustering),
}

def display_algorithm_table():
    """
    Display information about clustering algorithms in a formatted table.
    """
    table = pt.PrettyTable()
    table.field_names = ["No.", "Algorithm", "Parameters", "Scalability", "Usecase"]

    algorithms_info = [
        ["1", "K-Means", "number of clusters", "Very large n_samples", "General-purpose, flat geometry"],
        ["2", "Affinity Propagation", "damping, sample preference", "Not scalable with n_samples", "Uneven cluster sizes"],
        ["3", "Mean-Shift", "bandwidth", "Not scalable with n_samples", "Non-flat geometry"],
        ["4", "Spectral Clustering", "number of clusters", "Medium n_samples", "Few clusters, non-flat geometry"],
        ["5", "Ward Hierarchical", "number of clusters", "Large n_samples", "Connectivity constraints"],
        ["6", "Agglomerative", "linkage type, distance threshold", "Large n_samples", "Any pairwise distance"],
        ["7", "DBSCAN", "neighborhood size", "Very large n_samples", "Uneven clusters, non-flat geometry"],
        ["8", "OPTICS", "minimum cluster membership", "Very large n_samples", "Variable density"],
        ["9", "Gaussian Mixtures", "many", "Not scalable", "Density estimation, flat geometry"],
        ["10", "Birch", "branching factor", "Large n_samples", "Outlier removal"],
    ]

    for row in algorithms_info:
        table.add_row(row)

    print(table)

def main():
    print("Welcome to the Clustering Demo!")
    print("This demo showcases various clustering algorithms. Choose an option to get started.")

    df = None

    while True:
        print("\nOptions:")
        options_table = PrettyTable()
        options_table.field_names = ["Option", "Description"]
        options_table.add_rows([
            ["1", "View clustering algorithms"],
            ["2", "Create a default DataFrame"],
            ["3", "Simulate data and perform clustering"],
            ["4", "Create a custom DataFrame"],
            ["5", "Perform clustering on existing DataFrame"],
            ["6", "More options to create synthetic data"],
            ["7", "Evaluate the clustering"],
            ["8", "Plot the clustered data"],
            ["exit", "Quit"]
        ])
        print(options_table)
        user_input = input("Enter your choice: ").strip().lower()

        if user_input == 'exit':
            print("Exiting the demo. Goodbye!")
            break

        if user_input == '1':
            # Display clustering algorithm options
            display_algorithm_table()

        elif user_input == '2':
            # Define default column specifications
            column_specs = [
                {'name': 'height', 'reps': [180, 160, 120]},
                {'name': 'weight', 'reps': [80, 60, 30]},
                {'name': 'age', 'reps': [40, 35, 10]}
            ]
            
            # Step 1: Create the DataFrame
            try:
                df = cm.define_dataframe_structure(column_specs)
                if df is not None:
                    display_dataframe(df)
                else:
                    print("\n❌ DataFrame creation failed.")
            except Exception as e:
                print(f"\n❌ Error creating DataFrame: {e}")

        elif user_input == '3':
            # Step 2: Simulate data and perform clustering
            try:
                n_points = int(input("Enter the number of data points to simulate per cluster: ").strip())
                separation_factor = float(input("Enter the separation factor for the clusters: ").strip())
                display_algorithm_table()
                algorithm_choice = input("Enter the clustering algorithm (e.g., 'kmeans', 'dbscan'): ").strip()
                n_clusters = int(input("Enter the number of clusters to form: ").strip())
                # Call the intelligent_clustering function
                clustered_data = intelligent_clustering(df, n_clusters, separation_factor=separation_factor, n_points=n_points, algorithm=algorithm_choice)
                
                if clustered_data is not None:
                    display_dataframe(clustered_data, title="Clustered Data")
                    # Calculate and display descriptive statistics
                    stats = cm.calculate_descriptive_statistics(clustered_data)
                    if stats is not None:
                        display_descriptive_statistics(stats)
                else:
                    print("\n❌ Data simulation and clustering failed. Please check inputs.")
            except Exception as e:
                print(f"\n❌ Error simulating data and clustering: {e}")

        elif user_input == '4':
            # Custom DataFrame creation
            columns = []
            while True:
                col_name = input("Enter column name (or 'done' to finish): ").strip()
                if col_name.lower() == 'done':
                    break
                col_reps = input(f"Enter representative values for {col_name} (comma-separated): ").strip()
                try:
                    col_reps = [float(rep) for rep in col_reps.split(',')]
                    columns.append({'name': col_name, 'reps': col_reps})
                except ValueError:
                    print("Invalid input. Please enter numeric values separated by commas.")

            try:
                df = cm.define_dataframe_structure(columns)
                if df is not None:
                    display_dataframe(df)
                else:
                    print("\n❌ Custom DataFrame creation failed.")
            except Exception as e:
                print(f"\n❌ Error creating custom DataFrame: {e}")

        elif user_input == '5':
            display_algorithm_table()
            if df is not None:
                print("\nChoose a clustering algorithm to perform on the existing DataFrame:")
                for key, (name, _) in clustering_algorithms.items():
                    print(f"{key}: {name}")
                
                algo_choice = input("Enter the number corresponding to the algorithm: ").strip()
                if algo_choice in clustering_algorithms:
                    algo_name, algo_func = clustering_algorithms[algo_choice]
                    try:
                        # Perform clustering and check if the result is a DataFrame
                        clustered_data = algo_func(df)
                        
                        # Convert NumPy array results into a DataFrame if necessary
                        if isinstance(clustered_data, np.ndarray):
                            clustered_data = pd.DataFrame(clustered_data, columns=df.columns)
                        
                        if clustered_data is not None:
                            display_dataframe(clustered_data, title=f"{algo_name} Clustered Data")
                            # Calculate and display descriptive statistics
                            stats = cm.calculate_descriptive_statistics(clustered_data)
                            if stats is not None:
                                display_descriptive_statistics(stats)
                        else:
                            print(f"\n❌ {algo_name} clustering failed.")
                    except Exception as e:
                        print(f"\n❌ Error performing clustering: {e}")
                else:
                    print("Invalid algorithm choice.")
            else:
                print("Please create or load a DataFrame first (Option 2, 4 or 6).")

        elif user_input == '6':
            df = generate_custom_data()
            if df is not None:
                print("\nCustom data generated successfully.")
                display_dataframe(pd.DataFrame(df), title="Custom Data")
                # reshape the data for clustering
                if len(df.shape) == 1:
                    df = df.reshape(-1, 1)
            else:
                print("\n❌ Custom data generation failed.")

        elif user_input == '7':
            if df is not None:
                labels = intelligent_clustering(df, 3, separation_factor=1.0, n_points=100, algorithm="kmeans")
                if labels is not None:
                    evaluate_clustering(df, labels)
                else:
                    print("\n❌ Clustering labels not found. Please perform clustering first.")
            else:
                print("Please create or load a DataFrame first (Option 2, 4 or 6).")

        elif user_input == '8':
            if df is not None:
                labels = intelligent_clustering(df, 3, separation_factor=1.0, n_points=100, algorithm="kmeans")
                if labels is not None:
                    plot_clustering_data(df.values, labels)
                else:
                    print("\n❌ Clustering labels not found. Please perform clustering first.")
            else:
                print("Please create or load a DataFrame first (Option 2, 4 or 6).")
        else:
            print("Invalid option. Please try again.")

# Run the demo
if __name__ == "__main__":
    main()