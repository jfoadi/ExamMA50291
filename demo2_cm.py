import cluster_maker as cm

def main():
    # Define column specifications for the cluster centres
    column_specs = [
        {'name': 'X', 'reps': [1, 4, 2]},
        {'name': 'Y', 'reps': [2, 5, 8]}
    ]
    
    # Specifications for simulate_data function on how data points are distributed around the cluster centre points
    col_specs = {
        'X': {'distribution': 'normal', 'variance': 0.5},
        'Y': {'distribution': 'normal', 'variance': 0.5}
    }
    
    # Data with group separation factor of 3
    data = cm.intelligent_cluster_groups(
        column_specs=column_specs,
        n_points=100,
        col_specs=col_specs,
        group_separation_factor=3,
        random_state=42
    )
    
if __name__ == '__main__':
    main()
