from cluster_maker import (
    define_dataframe_structure,
    simulate_data,
    calculate_correlation,
    calculate_descriptive_statistics
)

import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    # Created input for the data with additional datapoints
    column_specs = [
        {'name': 'height', 'reps': [150, 160, 170, 180, 190]},
        {'name': 'weight', 'reps': [50, 60, 70, 80, 90]},
        {'name': 'age', 'reps': [20, 30, 40, 50, 60]},
        {'name': 'income', 'reps': [30000, 40000, 50000, 60000, 70000]}
    ]

    # Creation of DataFrame based on column_specs
    df = define_dataframe_structure(column_specs)
    print("DataFrame:")
    print(df)

    # Simulate 100 data points per group with column-specific distributions
    column_specs_simulate = {
        'height': {'distribution': 'normal', 'variance': 5},
        'weight': {'distribution': 'normal', 'variance': 10},
        'age': {'distribution': 'normal', 'variance': 5},
        'income': {'distribution': 'uniform', 'variance': 10000}
    }
    simulated_data = simulate_data(df, 100, column_specs_simulate, random_state = 30)
    print("\nSimulated Data:")
    print(simulated_data)

    crr = calculate_correlation(simulated_data)
    print("\nCorrelation Matrix:")
    print(crr)

    describe_data = calculate_descriptive_statistics(simulated_data)
    print("\nDescriptive Statistics:")
    print(describe_data)

    # Plotting the simulated data using a scatter matrix
    pd.plotting.scatter_matrix(simulated_data, alpha=0.2, figsize=(12, 12), diagonal='kde')
    plt.suptitle("Scatter Matrix of Simulated Data", y=1.02)
    plt.savefig("demo_cm_scatter_matrix.png")
    plt.show()


