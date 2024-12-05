
#demo file for testing cluster_maker

import cluster_maker as cm
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]

    print(f"Column specs:")
    for spec in column_specs:
        print(f"{spec['name']} : {spec['reps']}")

    #Print structured DataFrame using the define_dataframe_strucure function from dataframe_builder.py
    structured_df = cm.define_dataframe_structure(column_specs)
    print("Structures DataFrame:")
    print(structured_df)

    #Define column-specific simulation specs to control distribution of simulated data from centred data points
    col_specs = {
        'height': {'distribution': 'normal', 'variance': 5},
        'weight': {'distribution': 'normal', 'variance': 7},
        'age': {'distribution': 'normal', 'variance': 2}
    }

    #Simulate data from the structured DataFrame above
    #using the define_dataframe_strucure function from dataframe_builder.py
    print("Simulated Data:")
    simulated_data = cm.simulate_data(structured_df, n_points=100,col_specs=col_specs, random_state=None)
    print(simulated_data)


    #plot data on scatter plots to visualise data
    print("Scatter Plots for Data Visualisation:")
    
    columns = simulated_data.select_dtypes(include=['number']).columns
    column_number = len(columns)

    if column_number<2:
        print("Insufficient number of columns for visualisation, there must be atleast 2 columns. ")
    
    for i in range(column_number):
        for j in range(i + 1, column_number):
            x = columns[i]
            y = columns[j]
            plt.figure(figsize=(8, 6))
            plt.scatter(simulated_data[x], simulated_data[y], alpha=0.5, edgecolors='k')
            plt.title(f"{x} vs {y}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.grid(True)
            plt.show()