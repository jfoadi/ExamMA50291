###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import necessary libraries
try:
    import cluster_maker as cm
    import prettytable as pt
    import pandas as pd
except ImportError as e:
    print(f"Import error: {e}. Please make sure all necessary libraries are installed.")
    exit(1)


## Main
if __name__ == '__main__':
    # Create input for define_dataframe_structure
    print("Defining the structure of the dataframe with column specifications.")
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    
    # Create the dataframe, based on the above info
    print("Creating the dataframe based on the column specifications.")
    df = cm.define_dataframe_structure(column_specs)
    print("Dataframe structure defined:")
    
    # Display dataframe using PrettyTable
    table = pt.PrettyTable()
    table.field_names = ["Index"] + list(df.columns)
    for index, row in df.iterrows():
        table.add_row([index] + list(row))
    print(table)

    # Simulate 20 data points per group
    print("Simulating 20 data points per group.")
    data = cm.simulate_data(df, 20)

    # Try this first
    try:
        print("Calculating the correlation matrix for the simulated data.")
        crr = cm.calculate_correlation(data)  # Corrected function name
        print("Correlation matrix calculated:")
        
        # Display correlation matrix using PrettyTable
        corr_table = pt.PrettyTable()
        corr_table.field_names = [""] + list(crr.columns)
        for index, row in crr.iterrows():
            corr_table.add_row([index] + list(row))
        print(corr_table)
    except AttributeError as a:
        print(f"Attribute error: {a}")

    # Conclusion
    print("Everything is working fine.")
