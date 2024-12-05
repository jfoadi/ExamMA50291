## This demo file demonstrates visually the joint use 
## of define_dataframe_structure() and simulate_data().

## Import cluster_maker
import cluster_maker as cm

## Packages needed
import matplotlib.pyplot as plt

# Create input for define_dataframe_structure
column_specs = [
    {'name': 'height', 'reps': [180, 160, 120]},
    {'name': 'weight', 'reps': [80, 60, 30]},
    {'name': 'age', 'reps': [40, 35, 10]}
]
# Create the dataframe, based on the above info
df = cm.define_dataframe_structure(column_specs)
print("\nDataFrame structure:")
print(df)

# Simulate data points with column specifications
col_specs = {
    'height': {'distribution': 'normal', 'variance': 5},
    'weight': {'distribution': 'normal', 'variance': 3},
    'age': {'distribution': 'normal', 'variance': 2}
}

data = cm.simulate_data(df, n_points=50, col_specs=col_specs, random_state=0)
print("\nSimulated data points:")
print(data.head())

# Plot simulated data and representative points
plt.figure(figsize=(12, 6))

for i, col in enumerate(df.columns, start=1):
    # Plot simulated data histogram
    plt.hist(data[col], bins=20, alpha=0.6, label=f"Simulated {col}", color=f"C{i}")
    
    # Plot representative points as vertical lines
    for rep_point in df[col].dropna():
        plt.axvline(rep_point, color=f"C{i}", linestyle="--", label=f"Representative {col}")

# Add titles, labels, and legend
plt.title("Simulated Data vs Representative Points")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()