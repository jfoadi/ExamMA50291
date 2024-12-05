# To test intelligent_cluster from cluster_maker
import cluster_maker as cm

# Create input for define_dataframe_structure
column_specs = [
    {'name': 'A', 'reps': [180, 160, 120]},
    {'name': 'B', 'reps': [80, 60, 30]},
    {'name': 'C', 'reps': [40, 35, 10]}
]

# Create the dataframe, based on the above info
df = cm.define_dataframe_structure(column_specs)

# Create columns specs to simulate data, using both normal and uniform distributions and different variances
simulation_specs = {
    'A': {'distribution': 'normal', 'variance': 20},
    'B': {'distribution': 'uniform', 'variance': 10},
    'C': {'distribution': 'normal', 'variance': 3}
}

# Create intelligent clusters
clusters = cm.create_clusters(df, 100, col_specs=simulation_specs, random_state=42, group_separation=5.0)
cm.plot_clusters(clusters)

