import cluster_maker as cm
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]

df = cm.define_dataframe_structure(column_specs)
print("DataFrame:")
print(df)

# Simulate 50 data points per group
simulated_data = cm.simulate_data(df, n_points=50, col_specs={
    'height': {'distribution': 'normal', 'variance': 4},
    'weight': {'distribution': 'normal', 'variance': 2},
    'age': {'distribution': 'normal', 'variance': 1}
}, random_state=42)

print("\nSimulated Data:")
print(simulated_data.head())

plt.figure(figsize=(10, 6))
plt.scatter(simulated_data['height'], simulated_data['weight'], c=simulated_data['age'], cmap='viridis', edgecolors='k')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Simulated Data')
plt.colorbar(label='Age')
plt.grid(True)
plt.show()