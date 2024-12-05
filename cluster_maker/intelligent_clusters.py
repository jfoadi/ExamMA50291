import pandas as pd
import numpy as np

def create_intelligent_clusters(seed_df, num_groups, samples_per_group, separation):
    """
    Create well-separated clusters based on a seed DataFrame

    Parameters:
    - seef_df DataFrame created by define_dataframe_structure()
    - num_groups: Number of group[s to create
    - samples_per_group: Number of samples per group
    - separation: Separation between the groups

    Returns:
    - DataFrame contatining the generated clusters with a 'group' column 
    
    """
    # Initialize a empty list to hold the data
    data  =[]

    # Get the means of the seed DataFrame columns
    means = seed_df.mean()
    
    # Generate data for each group
    for i in range(num_groups):
        # Calculate the center for the current group
        center = means * (i * separation)
    
        # Generate random data around the center
        group_data =np.random.normal(loc=center, scale=5, size=(samples_per_group, len(seed_df.columns)))

        # Create a DataFrame for the current group
        group_df = pd.DataFrame(group_data, columns=seed_df.columns)
        group_df['group'] = i 

        # Append the group DataFrame to the data list
        data.append(group_df)

    # Concatenate all group DataFrames into a sinlge DataFrame
    final_df = pd.concat(data, ignore_index=True)

    return final_df