#demonstrate use define_dataframe_structure and simulate_data functions

# Import necessary libraries
import pandas as pd
import numpy as np
import cluster_maker as cm
import matplotlib.pyplot as plt

# Define the structure of the DataFrame
column_specs = [
    {'name': 'x', 'reps': [1, 2, 3, 4, 5]},
    {'name': 'y', 'reps': [5, 4, 3, 2, 1]}
]

# Create the DataFrame
df = cm.define_dataframe_structure(column_specs)

# Simulate data points around the representative points
data = cm.simulate_data(df, n_points=100)
print(data)

# Generate colors for each data point
colors = np.random.rand(len(data))
plt.scatter(data['x'], data['y'], c=colors, label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simulated Data Points')
plt.legend()
plt.show()





