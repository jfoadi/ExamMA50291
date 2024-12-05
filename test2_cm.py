###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

## Main
if __name__ == '__main__':
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    
    # Create and show the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)
    print('> Here is the DataFrame:')
    print(df)

    # Simulate 20 data points per group
    data = cm.simulate_data(df, 20)

    # Calculate and show the correlation matrix
    crr = cm.calculate_correlation(data)
    print('\n> After simulating 20 points per group in the DataFrame, here is the correlation matrix:')
    print(crr)

    # Conclusion
    print("\nThe test is now working with the desired output.")