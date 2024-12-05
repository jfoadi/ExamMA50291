###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries
import pandas as pd

## With two functions to calculate the correlation matrix and descriptive statistics of a DataFrame. 
## The functions are calculate_correlation and calculate_descriptive_statistics.    
## We use transposed data to include all columns in the descriptive statistics.
## Data.isnull().sum() is used to count the missing values in each column.
## include='all' is used to include all columns in the descriptive statistics.
## The correlation matrix is calculated using the corr() method.


"""
Calculate the correlation matrix and descriptive statistics of a DataFrame and input data user-defined specifications.

Parameters:
- data (pd.DataFrame): The DataFrame to analyse.(data type: pd.DataFrame or None)
- column_specs (list of dict): A list where each dictionary defines a numerical column.(data type: list of dict)
- missing_values (str): The value used to represent missing values in the data (default: 'NaN').(data type: str)

Returns: correlation_matrix, stats
"""

## Function to calculate the correlation matrix
def calculate_correlation(data):
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats

#handling should be informative for calculate_correlation and calculate_descriptive_statistics
try:
#calculate_correlation
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")
    correlation_matrix = calculate_correlation(data)
#calculate_descriptive_statistics
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")
    stats = calculate_descriptive_statistics(data)
    return correlation_matrix, stats
except TypeError as e:
    print(f"Error in data_analyser: {e}")
    return None
except Exception as e:
    print(f"Error in data_analyser: {e}")
    return None



