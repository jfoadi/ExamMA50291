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
    the function calculate_correlation calculates the correlation matrix for the given data.
    parameters: Dataframe called data
    returns: dataframe containing the correlation matrix of the data.
    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    this function gives the descriptive statistics for the data like mean, count, standard deviation, minimum and maximum values, and the number of missing values.

    parameters: Dataframe called data
    returns: Dataframe containing descriptive statistics for each column in the input dataframe including mean, count, standard deviation,25%,50% and 75% percentiles,
             minimum value, maximum value, missing values for numerical columns and
             most frequent value and its frequency, number of unique values for non numerical columns.
    """
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats