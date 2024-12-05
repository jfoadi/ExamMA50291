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
        data: Is a pandas DataFrame and the input DataFrame contains numerical data.
    
    Returns:
        pd.DataFrame: A DataFrame containing the correlation matrix of the input data,
        showing pairwise correlation coefficients between columns.
    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix

    
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
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats