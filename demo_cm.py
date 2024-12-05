###
## demo_cm.py
## Demonstrates the joint use of define_dataframe_structure() and simulate_data(),
## including additional analysis with correlation and descriptive statistics.
## J. Foadi - University of Bath - 2024
###

# Import necessary libraries
try:
    import cluster_maker as cm
    import pandas as pd
    from prettytable import PrettyTable
except ImportError as e:
    print(f"\n❌ Error importing libraries: {e}")
    print("Please ensure all required libraries are installed.")
    exit(1)

# Function to display DataFrame using PrettyTable
def display_dataframe(df, title="DataFrame"):
    try:
        table = PrettyTable(df.columns.tolist())
        for row in df.itertuples(index=False):
            table.add_row(row)
        print(f"\n{title}:\n")
        print(table)
    except Exception as e:
        print(f"\n❌ Error displaying DataFrame: {e}")

# Function to display a correlation matrix using PrettyTable
def display_correlation_matrix(correlation_matrix):
    try:
        table = PrettyTable()
        table.field_names = [""] + correlation_matrix.columns.tolist()
        for row in correlation_matrix.itertuples():
            table.add_row([row.Index] + list(row[1:]))
        print("\nCorrelation Matrix:")
        print(table)
    except Exception as e:
        print(f"\n❌ Error displaying correlation matrix: {e}")

# Function to display descriptive statistics using PrettyTable
def display_descriptive_statistics(stats):
    """
    Calculate descriptive statistics (mean, median, std, etc.) for the given DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        pd.DataFrame: DataFrame with descriptive statistics.
    """
    try:
        table = PrettyTable()
        table.field_names = ["Statistic"] + stats.columns.tolist()
        for row in stats.itertuples():
            table.add_row([row.Index] + list(row[1:]))
        print("\nDescriptive Statistics:")
        print(table)
    except Exception as e:
        print(f"\n❌ Error displaying descriptive statistics: {e}")



# Main function
def main():
    """
    Main function to demonstrate the joint use of define_dataframe_structure() 
    and simulate_data(), along with additional data analysis like descriptive 
    statistics and correlation matrix calculation.
    """

    print("Welcome to the Cluster Maker Demo!")
    print("This demo showcases the creation of a structured DataFrame, simulated data, and additional analyses.")

    while True:
        print("\nLet's get started!")
        options_table = PrettyTable(["Option", "Description"])
        options_table.add_row(["1", "Create a default DataFrame"])
        options_table.add_row(["2", "Simulate data"])
        options_table.add_row(["3", "Create a custom DataFrame"])
        options_table.add_row(["exit", "Quit the demo"])
        print("\nAvailable Options:")
        print(options_table)

        user_input = input("\nEnter an option (1, 2, 3, or 'exit'): ").strip()
        if user_input == 'exit':
            print("Exiting the demo. Goodbye!")
            break

        if user_input == '1':
            # Define default column specifications
            column_specs = [
                {'name': 'height', 'reps': [180, 160, 120]},
                {'name': 'weight', 'reps': [80, 60, 30]},
                {'name': 'age', 'reps': [40, 35, 10]}
            ]
            
            # Step 1: Create the DataFrame
            try:
                df = cm.define_dataframe_structure(column_specs)
                if df is not None:
                    display_dataframe(df)
                    # Calculate and display descriptive statistics
                    stats = cm.calculate_descriptive_statistics(df)
                    if stats is not None:
                        display_descriptive_statistics(stats)
                else:
                    print("\n❌ DataFrame creation failed.")
            except Exception as e:
                print(f"\n❌ Error creating DataFrame: {e}")

        elif user_input == '2':
            # Step 2: Simulate data
            try:
                n_points = int(input("Enter the number of data points to simulate per representative: ").strip())
                simulated_data = cm.simulate_data(df, n_points)
                
                if simulated_data is not None:
                    display_dataframe(simulated_data, title="Simulated Data")
                    # Calculate and display correlation matrix
                    correlation_matrix = cm.calculate_correlation(simulated_data)
                    if correlation_matrix is not None:
                        display_correlation_matrix(correlation_matrix)
                else:
                    print("\n❌ Data simulation failed. Please check inputs.")
            except Exception as e:
                print(f"\n❌ Error simulating data: {e}")

        elif user_input == '3':
            # Custom DataFrame creation
            columns = []
            while True:
                col_name = input("Enter column name (or 'done' to finish): ").strip()
                if col_name.lower() == 'done':
                    break
                col_reps = input(f"Enter representative values for {col_name} (comma-separated): ").strip()
                try:
                    col_reps = [float(rep) for rep in col_reps.split(',')]
                    columns.append({'name': col_name, 'reps': col_reps})
                except ValueError:
                    print("Invalid input. Please enter numeric values separated by commas.")

            try:
                df = cm.define_dataframe_structure(columns)
                if df is not None:
                    display_dataframe(df)
                    # Calculate and display descriptive statistics
                    stats = cm.calculate_descriptive_statistics(df)
                    if stats is not None:
                        display_descriptive_statistics(stats)
                else:
                    print("\n❌ Custom DataFrame creation failed.")
            except Exception as e:
                print(f"\n❌ Error creating custom DataFrame: {e}")

        else:
            print("Invalid input. Please enter '1', '2', '3', or 'exit'.")

    print("\nDemo completed successfully! 🚀")

# Run the demo
if __name__ == "__main__":
    main()
