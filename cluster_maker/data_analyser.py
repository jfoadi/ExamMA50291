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
    Calculate the correlation matrix of a DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame

    Returns:
        pd.DataFrame: The correlation matrix
    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for a DataFrame, along with the number of missing values.

    Parameters:
        data (pd.DataFrame): The DataFrame to analyse

    Returns:
        pd.DataFrame: A DataFrame with descriptive statistics for each column of the data, including:
                       - count, mean, std, min, max, 25%, 50%, 75% for numeric data
                       - count, unique, top, freq for object data
                      The number of missing values for each column is also included in an additional column.
    """
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats