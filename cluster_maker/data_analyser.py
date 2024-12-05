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
    Calculate the correlation matrix of a dataframe.

    Parameters:
        data (pd.DataFrame): The DataFrame to compute the pairwise correlation of its columns.

    Returns:
        pd.DataFrame: DataFrame containing the correlation matrix of the input data.

    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Generate the descriptive statistics of a dataframe.

    Parameters:
        data (pd.DataFrame): The DataFrame to calculate the descriptive statistics of its columns.

    Returns:
        pd.DataFrame: DataFrame containing the descriptive statistics of the input data columns and the number of missing values.
        Columns:
            column  | count  |  mean  |  std  |  min  |  25%  |  50%  |  75%  |  max  |  missing_values
    """
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats