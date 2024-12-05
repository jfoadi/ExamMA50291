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
    print(df)

    # Simulate 20 data points per group
    data = cm.simulate_data(df, 20)

    # Try this first
    try:
        # not the right function for correlation matrix so make sure to display error not pass over it
        crr = cm.corre1ation_matrix(data)
        print(crr)
    except AttributeError as a:
        print(f"AttributeError: {a} - The function may not exists in the cluster_maker module")
    except Exception as e:
        print(f"An error occured {e}")

    try:
        # put the right function in for correlation matrix and display it
        crr = cm.calculate_correlation(data)
        print(crr)
    except AttributeError as a:
        print(f"AttributeError: {a} - The function may not exists in the cluster_maker module")
    except Exception as e:
        print(f"An error occured {e}")

    # Conclusion
    print("Is everything really working?")