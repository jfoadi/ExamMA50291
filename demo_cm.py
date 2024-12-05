## Import cluster_maker
import cluster_maker as cm

## Main
if __name__ == '__main__':
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'MA50290', 'reps': [65, 75, 40]},
        {'name': 'MA50291', 'reps': [80, 90, 65]},
        {'name': 'MA50297', 'reps': [75, 55, 50]},
        {'name': 'MA50299', 'reps': [75, 60, 60]}
    ]
    print(column_specs)
    
    # Create the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)
    print(df)

    distribution_specs = {
        'MA50290': {'disribution':'normal', 'variance':6},
        'MA50291': {'disribution':'normal', 'variance':4},
        'MA50297': {'disribution':'normal', 'variance':9},
        'MA50299': {'disribution':'normal', 'variance':8}
    }

    # Simulate 10 data points per group
    data = cm.simulate_data(df, 10, distribution_specs)

    #Round data so they represent possible marks
    data = data.round(0)

    print(data)
