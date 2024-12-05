import cluster_maker as cm
import matplotlib.pyplot as plt

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
    'A': {'distribution': 'normal', 'variance': 25},
    'B': {'distribution': 'uniform', 'variance': 15},
    'C': {'distribution': 'normal', 'variance': 3}
}

# Simulate 100 data points per group, with the above specs and a random seed
data = cm.simulate_data(df, 100, col_specs=simulation_specs, random_state=42)


# Export the simulated data to a CSV file and in formatted text
cm.export_to_csv(data, 'demo_simulated_data.csv', delimiter=",", include_index=False)
cm.export_formatted(data, 'demo_simulated_formatted_data.txt', include_index=False)


# Plot the distributions of the simulated data for visual demonstration
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].hist(data['A'], bins=20, color='skyblue', edgecolor='black')
axs[0].set_title('Distribution A')
axs[0].set_xlabel('A')
axs[0].set_ylabel('Frequency')

axs[1].hist(data['B'], bins=20, color='salmon', edgecolor='black')
axs[1].set_title('Distribution B')
axs[1].set_xlabel('B')
axs[1].set_ylabel('Frequency')

axs[2].hist(data['C'], bins=20, color='lightgreen', edgecolor='black')
axs[2].set_title('Distribution C')
axs[2].set_xlabel('C')
axs[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()


