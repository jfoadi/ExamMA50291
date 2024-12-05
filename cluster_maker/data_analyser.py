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
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
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
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats