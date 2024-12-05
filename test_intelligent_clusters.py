import pandas as pd
from cluster_maker.intelligent_clusters import create_separated_clusters
from cluster_maker.visualise_clusters import visualise_clusters

def get_user_input():
    """
    Prompts the user for key parameters such as distributions, variances, and separation factor, with error handling.
    """
    def get_positive_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Value must be positive. Try again.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def get_distribution(prompt):
        while True:
            dist = input(prompt).strip().lower()
            if dist in ['normal', 'uniform']:
                return dist
            else:
                print("Invalid distribution. Please enter 'normal' or 'uniform'.")
    
    # Get column specifications from the user
    print("Enter column specifications for the seed data (height, weight, age).")
    
    height_mean = get_positive_float("Enter the mean height (e.g., 180): ")
    height_variance = get_positive_float("Enter the variance for height (e.g., 5): ")
    
    weight_mean = get_positive_float("Enter the mean weight (e.g., 80): ")
    weight_variance = get_positive_float("Enter the variance for weight (e.g., 10): ")
    
    age_mean = get_positive_float("Enter the mean age (e.g., 40): ")
    age_variance = get_positive_float("Enter the variance for age (e.g., 3): ")
    
    # Get distribution types
    height_dist = get_distribution("Enter the distribution type for height (normal, uniform): ")
    weight_dist = get_distribution("Enter the distribution type for weight (normal, uniform): ")
    age_dist = get_distribution("Enter the distribution type for age (normal, uniform): ")
    
    # Get the separation factor (ensure it is positive)
    separation_factor = get_positive_float("Enter the separation factor (e.g., 15): ")
    
    # Get the number of points per group (ensure it is a positive integer)
    while True:
        try:
            n_points = int(input("Enter the number of data points per group (e.g., 50): "))
            if n_points <= 0:
                print("The number of data points must be a positive integer. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Create the column_specs list based on user input
    column_specs = [
        {'name': 'height', 'reps': [height_mean, height_mean - 20, height_mean - 60]},
        {'name': 'weight', 'reps': [weight_mean, weight_mean - 20, weight_mean - 50]},
        {'name': 'age', 'reps': [age_mean, age_mean - 5, age_mean - 30]}
    ]
    
    # Create the col_specs dictionary based on user input
    col_specs = {
        'height': {'distribution': height_dist, 'variance': height_variance},
        'weight': {'distribution': weight_dist, 'variance': weight_variance},
        'age': {'distribution': age_dist, 'variance': age_variance}
    }
    
    return column_specs, col_specs, separation_factor, n_points

def test_create_separated_clusters():
    """
    Test the create_separated_clusters function to ensure it generates well-separated clusters
    based on the separation factor, with user-defined parameters.
    """
    print("Welcome to the Cluster Simulation!")
    column_specs, col_specs, separation_factor, n_points = get_user_input()
    
    # Generate separated clusters with user-defined parameters
    simulated_data = create_separated_clusters(
        column_specs=column_specs,
        n_points=n_points,
        col_specs=col_specs,
        separation_factor=separation_factor,
        random_state=42
    )

    # Check if the data was generated and contains the expected columns
    if simulated_data is None:
        print("Error in data generation. Please check the input values.")
        return
    
    # Check for required columns
    required_columns = ['group', 'height', 'weight', 'age']
    for col in required_columns:
        if col not in simulated_data.columns:
            print(f"Column '{col}' is missing.")
            return

    # Print a sample of the generated data
    print(simulated_data.head())

    # Check if the groups are separated as expected
    print("Group distribution:")
    print(simulated_data['group'].value_counts())

    # Visualize the clusters
    visualise_clusters(simulated_data, col_specs)

# Run the test
if __name__ == '__main__':
    test_create_separated_clusters()