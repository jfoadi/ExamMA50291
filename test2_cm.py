###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

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
    
    # Create the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)
    print(f'Data:\n{df}')

    # Simulate 20 data points per group
    # cm.simulate_data(df, 20) was not including randomness (just repeated the same data)
    # Added col_specs to include randomness
    col_specs = {

        'height': {
            'distribution': 'normal',
            'variance': 4.0
        },
        'weight': {
            'distribution': 'uniform',
            'variance': 5.0
        },
        'age': {
            'distribution': 'normal',
            'variance': 2.0
        }
    }
    data = cm.simulate_data(df, 20, col_specs=col_specs)
    print(f'\nSimulated data:\n{data}')

    # Try this first
    try:
        # corre1ation_matrix is not a function in the cluster_maker package
        # so this bit of code never ran
        # Changed to calculate_correlation
        crr = cm.calculate_correlation(data)
        # Added a print statement to show the correlation matrix
        # To make sure this part of the code is working
        print(f'\nCorrelation Matrix:\n{crr}')
    except AttributeError as a:
        pass

    # Conclusion
    print("Is everything really working?") # Now it is :)