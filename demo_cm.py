import cluster_maker as cm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    """
    Demonstrates the use of define_dataframe_structure() and simulate_data()
    from the cluster_maker package with a visual output using Matplotlib.
    """
    # Step 1: Define the seed DataFrame
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    df = cm.define_dataframe_structure(column_specs)
    print("Seed DataFrame:")
    print(df)

    # Step 2: Specify simulation parameters
    col_specs = {
        'height': {'distribution': 'normal', 'variance': 5},
        'weight': {'distribution': 'normal', 'variance': 10},
        'age': {'distribution': 'normal', 'variance': 3}
    }

    # Step 3: Generate simulated data
    simulated_data = cm.simulate_data(df, n_points=100, col_specs=col_specs, random_state=42)
    print("\nSimulated DataFrame:")
    print(simulated_data)

    # Step 4: Visualize the results
    visualize_simulation(simulated_data)

def visualize_simulation(simulated_data, seed_df=None, col_specs=None):
    """
    Creates histograms for simulated data where bars are split into fractions
    based on age categories and includes a cluster plot.
    
    Parameters:
        simulated_data (pd.DataFrame): The generated data to visualize.
        seed_df (pd.DataFrame, optional): The original DataFrame used as seed values.
        col_specs (dict, optional): Column-specific simulation settings, including variance.
    """
    # Define age group categories
    bins = [0, 20, 30, 40, 50, 100]  # Example age bins
    labels = ['10-20', '20-30', '30-40', '40-50', '50+']
    simulated_data['age_group'] = pd.cut(simulated_data['age'], bins=bins, labels=labels, right=False)

    # Histograms for individual columns, with fractions by age group
    for column in simulated_data.columns:
        if column == 'age_group':  # Skip age group column for plotting
            continue

        plt.figure(figsize=(8, 6))

        # Create stacked histogram
        age_groups = simulated_data['age_group'].unique()
        bottom = None
        for age_group in age_groups:
            group_data = simulated_data[simulated_data['age_group'] == age_group]
            counts, bin_edges = np.histogram(group_data[column], bins=20, range=(simulated_data[column].min(), simulated_data[column].max()))
            if bottom is None:
                bottom = counts
                plt.bar(bin_edges[:-1], counts, width=bin_edges[1] - bin_edges[0], label=age_group, align='edge')
            else:
                plt.bar(bin_edges[:-1], counts, bottom=bottom, width=bin_edges[1] - bin_edges[0], label=age_group, align='edge')
        
        # Mark means and variance ranges
        if seed_df is not None and col_specs is not None and column in seed_df.columns and column in col_specs:
            for mean in seed_df[column]:
                variance = col_specs[column].get('variance', 1)

                # Add vertical lines for mean and variance
                plt.axvline(mean, color='blue', linestyle='--', linewidth=1, label='Mean')
                plt.axvline(mean - variance, color='green', linestyle=':', linewidth=1, label='Mean - Variance')
                plt.axvline(mean + variance, color='green', linestyle=':', linewidth=1, label='Mean + Variance')

        plt.title(f"Histogram of {column} with Age Group Fractions")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.legend(title="Age Group")
        plt.show()

    # Scatter Graph of Height vs Weight by Age Group
    plt.figure(figsize=(10, 6))
    colors = {'10-20': 'blue', '20-30': 'green', '30-40': 'orange', '40-50': 'purple', '50+': 'red'}

    for age_group, color in colors.items():
        group_data = simulated_data[simulated_data['age_group'] == age_group]
        plt.scatter(group_data['height'], group_data['weight'], alpha=0.6, s=40, c=color, label=age_group)

    plt.title("Scatter Graph of Height vs. Weight by Age Group")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend(title="Age Group")
    plt.show()

if __name__ == "__main__":
    main()