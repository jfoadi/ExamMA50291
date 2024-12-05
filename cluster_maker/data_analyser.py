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
    Calculate the correlation matrix of a dataset.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: Correlation Matrix 

    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Generate descriptive statistics of a dataset.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the data to be analysed.

    Returns:
        pd.DataFrame or Series: contains descriptive stats (mean, sd, min, max, percentiles, number of missing values)
    """
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats