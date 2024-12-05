## 6) Write a demo file, called "demo_cm.py", that demonstrates
## visually the joint use of define_dataframe_structure() and 
## simulate_data().
## [20]

import cluster_maker as cm
import pandas as pd
import numpy as np
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: matplotlib library is not installed. Please install it using 'pip install matplotlib'.")
    plt = None  

"""
This demo_cm.py file uses the cluster_maker package to visually demonstrate the joint use of
define_dataframe_structure() and simulate_data() functions. The define_dataframe_structure() function
is used to create a numerical DataFrame structure based on defined numbers. The simulate_data() function
is used to simulate data points based on the dataframe structure. The simulated data is then plotted
to visualise the clusters.
"""
    
def main():
    """
    Main function uses define_dataframe_structure() and simulate_data() functions from cluster_maker package.
    
    1. Define the centre of the clusters in column_specs. These are put into a DataFrame using define_dataframe_structure().
    2. Input specifications to simulate data points around the cluster. These are the number of points to simulate per cluster,
    the distribution and variance of the data points and the random state. 
    3. Simulate data points around the cluster using simulate_data() function.
    4. Plot the simulated data points to visualise the clusters.
    
    Returns:
        Scatter plot of the simulated data points.
    """
    column_specs = [
        {'name': 'X', 'reps': [1, 6, 4]},
        {'name': 'Y', 'reps': [1, 2, 5]}
    ]
    
    seed_df = cm.define_dataframe_structure(column_specs)
    print("DataFrame structure:")
    print(seed_df)

    n_points = 100  # Number of points to simulate per cluster
    
    col_specs = {
        'X': {'distribution': 'normal', 'variance': 0.5},
        'Y': {'distribution': 'normal', 'variance': 0.5}
    }

    data = cm.simulate_data(seed_df, n_points=n_points, col_specs=col_specs, random_state=42)

    number_of_clusters = len(seed_df)
    cluster_labels = []
    for cluster_id in range(number_of_clusters):
        cluster_labels.extend([cluster_id] * n_points) # how many points per cluster
    data['Cluster'] = cluster_labels # Add cluster labels to the DataFrame for plotting

    cm.plot_clusters(data, x='X', y='Y', cluster_col='Cluster', title='Simulated Data from cluster_maker', save_file='simulated_data.png')

    cm.export_formatted(data, 'simulated_data.txt', include_index=True)
    cm.export_to_csv(data, 'simulated_data.csv', delimiter=",", include_index=True)
    
    
if __name__ == '__main__':
    main()
    
    