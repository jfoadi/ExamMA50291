import cluster_maker as cm

def main():
    """
    Main function generates well separated cluster groups using the intelligent_cluster_groups function.
    
    Steps:
    1. Define cluster centres using a data frame
    2. Specify how the point are distributed around the cluster centres
    3. Generate data points around the cluster centres with a separation factor to make sure clusters are well separated. 
    
        Group separation factor: determines how much the clusters are separated. If it is equal to 1, then nothing changes, 
        if it is less than 1, then clusters will be closer to each other, and if it is greater than 1, then clusters will be 
        further separated. 
    
    Parameters:
        None
        
    Returns:
        None
    """
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
    group_separation_factor = 3

    # Data with group separation factor of 3
    data, seed_df = cm.intelligent_cluster_groups(
        column_specs=column_specs,
        n_points=100,
        col_specs=col_specs,
        group_separation_factor=group_separation_factor,
        random_state=42
    )
    cm.plot_clusters(data, seed_df, title='Cluster Groups with a separation factor of '+ str(group_separation_factor), save_file='cluster_groups_separation_factor_'+str(group_separation_factor)+'.png')
    cm.export_formatted(data, 'clusters_separation_factor_'+str(group_separation_factor)+'.txt', include_index=True)
    cm.export_to_csv(data, 'clusters_separation_factor_'+str(group_separation_factor)+'.csv', delimiter=",", include_index=True)
    
if __name__ == '__main__':
    main()
