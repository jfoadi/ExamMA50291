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
    Calculates the correlation matrix for the given data.

    Input:
    data (DataFrame): The input data for which the correlation matrix needs to be calculated.

    Output:
    correlation_matrix (DataFrame): The correlation matrix of the input data.
    """

    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for the given data. The descritive statistics include count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values for each column of the data 
    includes 
    - Count
    - Mean 
    - Standard deviation 
    - Minimum value
    - 25th percentile
    - Median or 50th percentile
    - 75th percentile
    - Maximum value
    - Number of missing values in each column.

    Input:
    data (pandas.DataFrame): The data for which descriptive statistics are to be calculated.

    Output:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for each column of the data.
                        Rows represent the variables and columns represent the statistics.

    """

    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats