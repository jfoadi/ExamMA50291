###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries
import pandas as pd

## Function to calculate the correlation matrix
def calculate_correlation(data):
    """
    Calculate the correlation matrix for the given dataframe.
        pairwise correlation of columns, excluding NaN/null values.

    Parameters:
        data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame: The correlation matrix.
    """
    # Check if the input is a DataFrame
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        # Handle non-numeric data
        if not any(data.dtypes.apply(lambda x: x in ['int64', 'float64'])):
            raise ValueError("No numeric data found in DataFrame")
        # Handle empty data
        if data.empty:
            raise ValueError("DataFrame is empty")

        # Calculate the correlation matrix
        correlation_matrix = data.corr()
        
        # Return the correlation matrix
        return correlation_matrix

    except Exception as e:
        print(f"Error calculating correlation: {e}")
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculates descriptive statistics for the given dataframe.
    Depending on the data type, the output will include count, mean, std, min, 25%, 50%, 75%, max.
    Or for object data, the output will include count, unique, top, freq.

    Parameters:
        data (pd.DataFrame): The input data.
    
    Returns:
        pd.DataFrame: Descriptive statistics for the input data.
    """

    # Check if the input is a DataFrame
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        # Handle empty data
        if data.empty:
            raise ValueError("DataFrame is empty")
        
        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
            
        return stats
    
    except Exception as e:
        print(f"Error calculating descriptive statistics: {e}")
        return None