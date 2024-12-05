###
## To test demonstrate visually the joint use of define_dataframe_structure() and simulate_data()
## Adam Young - University of Bath - 2024
###


## Import necessary libraries, give a relevent error message if they are not installed correctly.
try:
    import numpy as np
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Numpy installed. Please install it to use this code ***")
try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Matplotlib installed. Please install it to use this code ***")
try:
    import pandas as pd
except ImportError:
    raise ImportError("*** ERROR: You do not currently have Pandas installed. Please install it to use this code ***")

import cluster_maker as cm

## Main
if __name__ == '__main__':

    print('\nDEMO: Average exam mark for 3 different University courses')

    # Define the structure of the DataFrame with seed values
    column_specs = [
        {'name': 'DataScience', 'reps': [70, 73, 81]},      # Seed points for Data Science average mark
        {'name': 'MachineLearning', 'reps': [62, 54, 61]},  # Seed points for Machine Learning average mark
        {'name': 'TimeSeries', 'reps': [68, 69, 71]}        # Seed points for Time Series average mark
    ]

    # Create the DataFrame using the specified structure
    df = cm.define_dataframe_structure(column_specs)

    # Print the DataFrame
    print('\n> Here is the DataFrame with seed values for the 3 courses:')
    print(df)

    # Simulate 250 data points per representative using the seed DataFrame
    col_specs = {
        'DataScience': {'distribution': 'normal', 'variance': 3},
        'MachineLearning': {'distribution': 'normal', 'variance': 4},
        'TimeSeries': {'distribution': 'uniform', 'variance': 2}
    }

    simulated_data = cm.simulate_data(df, n_points=250, col_specs=col_specs, random_state=666)

    print('\n> Successfully simulated 250 marks per module')
    print('> Open the file Demo_Plot.py to see a visual representation of the simulated data\n')

    # Plot the simulated data:

    plt.figure(figsize=(10, 6))

    # Plot the distribution of Data Science marks
    plt.hist(simulated_data['DataScience'], bins=15, alpha=0.5, label='Data Science mark (%)', color='skyblue', edgecolor='black')

    # Plot the distribution of Machine Learning marks
    plt.hist(simulated_data['MachineLearning'], bins=15, alpha=0.5, label='Machine Learning mark (%)', color='lightgreen', edgecolor='black')

    # Plot the distribution of TimeSeries
    plt.hist(simulated_data['TimeSeries'], bins=15, alpha=0.5, label='Time Series mark (%)', color='salmon', edgecolor='black')

    # Adding titles and labels
    plt.title('Distributions of DataScience, MachineLearning, and TimeSeries marks')
    plt.xlabel('Mark (%)')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    plt.savefig('Demo_Plot.png') 
    plt.close()

