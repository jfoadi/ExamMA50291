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
    Calculate the correlation matrix for a given DataFrame

    Parameters:
        data (pd.DataFrame): Data for which correlation should be calculated

    Returns:
        pd.DataFrame: Correlation matrix for data

    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")

    try:
        # Calculate the correlation matrix
        correlation_matrix = data.corr()

        # Return the correlation matrix
        return correlation_matrix
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for a given DataFrame, including number of missing values
    
    Parameters:
        data (pd.DataFrame): Data for which descriptive statistics should be calculated
    Returns:
        pd.DataFrame: Descriptive statistics for data

    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")
    
    try:
        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()    
        return stats
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
