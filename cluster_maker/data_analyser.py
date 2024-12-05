###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries

# Check to see if pandas and numpy are installed
try:
    import pandas as pd
except ImportError:
    print("Error: pandas library is not installed. Please install it using 'pip install pandas'.")
    pd = None  
try:
    import numpy as np
except ImportError:
    print("Error: numpy library is not installed. Please install it using 'pip install pandas'.")
    np = None  

## Function to calculate the correlation matrix
def calculate_correlation(data):
    """
    Calculate the correlation matrix of a DataFrame.
    
    Parameters:
        data: Is a pandas DataFrame and the input DataFrame contains numerical data.
    
    Returns:
        pd.DataFrame: A DataFrame containing the correlation matrix of the input data,
        showing pairwise correlation coefficients between columns.
    """
    # Exception handling to check the input data doesn't contain any errors
    try:
        if not isinstance(data, pd.DataFrame): # Check if input is a pandas DataFrame
            raise TypeError("Data must be a pandas DataFrame.")
        if data.empty: # Check if DataFrame is empty
            raise ValueError("Input DataFrame is empty.")
        if data.isnull().values.any():  # Check for null data values
            raise ValueError("Input DataFrame contains NaN values.")
        if np.isinf(data.values).any(): # check for infinite values
            raise ValueError("Input DataFrame contains infinite values.")
        # selects only numeric data
        numeric_data = data.select_dtypes(include=[np.number])
        if numeric_data.empty:
            raise ValueError("No numeric columns found in the DataFrame.")
        # Calculate the correlation matrix
        correlation_matrix = numeric_data.corr()
        
        # Return the correlation matrix
        return correlation_matrix
    
    except Exception as e:
        print(f"An error occurred in calculate_correlation: {e}")
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for each column of a DataFrame.
    It provides a summary of key statistics and includes the missing null values in each column.
    
    Parameters:
        data: Is a pandas DataFrame and the input DataFrame contains numerical data.
    
    Returns:
        pd.DataFrame: A DataFrame containing the descriptive statistics of the input data,
                      such as mean, standard deviation, minimum, maximum, null values. 
    """
    try:
        if not isinstance(data, pd.DataFrame):   # Check if input is a pandas DataFrame
            raise TypeError("Input data must be a pandas DataFrame.")
        if data.empty:   # Check if data is empty
            raise ValueError("Input DataFrame is empty.")
        if np.isinf(data.values).any():  # Warn about infinite values in columns
            print("Warning: Input DataFrame contains infinite values in numeric columns.")

        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()

        return stats
    
    except Exception as e:
        print(f"An error occurred in calculate_descriptive_statistics: {e}")
        return None
