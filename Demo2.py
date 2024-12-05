###
## To test the use of intelligent_clusters.py in the cluster_maker package
## Adam Young - University of Bath - 2024
###

# Import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Matplotlib installed. Please install it to use this code ***")

# Import the cluster_maker package
import cluster_maker as cm



# 1) Create input for define_dataframe_structure
column_specs = [
    {'name': 'height', 'reps': [180, 160, 120]},
    {'name': 'weight', 'reps': [80, 60, 30]},
    {'name': 'age', 'reps': [40, 35, 10]}
]

# 2) Create the seed dataframe using define_dataframe_structure
df = cm.define_dataframe_structure(column_specs)
print("\n> Seed DataFrame:")
print(df)

# 3) Simulate data (250 data points per group)
data = cm.simulate_data(df, 250)

# 4) Now create separated clusters using intelligent_clusters
# Parameters: df (seed dataframe), n_points (number of points per group), group_separation (controls separation)
separated_clusters = cm.create_separated_clusters(df, n_points=20, group_separation=30, random_state=42)

print('\n> After simulating 250 data poitns for each group, find the clusters plotted in the file Demo2.png') 

# Plot and save to file Demo2.png
plt.figure(figsize=(8, 6))
plt.scatter(separated_clusters['height'], separated_clusters['weight'], c=separated_clusters['age'], cmap='viridis')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Separated Clusters')
plt.colorbar(label='Age')
plt.savefig('Demo2.png')  
plt.close()