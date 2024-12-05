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

    col_specs = {
    'height': {'distribution': 'normal', 'variance': 1},
    'weight': {'distribution': 'normal', 'variance': 1},
    'age': {'distribution': 'normal', 'variance': 1}
    }


    
    # Create the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)
    print(df)

    # Simulate 20 data points per group
    data = cm.simulate_data(df, 20, col_specs) # Simulates 20 points per group, following randomness outlined in col_specs
    # random_state is left blank so that the randomness is not fixed
    # Try this first
    try:
        crr = cm.calculate_correlation(data)
    except AttributeError as a:
        print(f"AttributeError: {a}")
        pass

    # Conclusion
    print("Is everything really working?")
    print(data)
    print(crr)