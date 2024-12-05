###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries
import pandas as pd
import numpy as np

## Function to calculate the correlation matrix
def calculate_correlation(data):
    """
    Calculates the correlation matrix for the given data.

    Input:
    data (DataFrame or array-like): The input data for which the correlation matrix needs to be calculated.

    Output:
    correlation_matrix (DataFrame): The correlation matrix of the input data.
    """
    
    try:
        # Check if the input data is a DataFrame
        if not isinstance(data, pd.DataFrame):
            # Try converting data into a DataFrame
            data = pd.DataFrame(data)
        
        # Check if all columns are numeric
        if not data.select_dtypes(include=np.number).columns.equals(data.columns):
            raise ValueError("All columns of the data must be numeric to calculate the correlation matrix.")
        
        # Calculate the correlation matrix
        correlation_matrix = data.corr()
        
        # Check for missing values in columns
        missing_columns = data.columns[data.isnull().any()].tolist()
        if missing_columns:
            print("The following columns have missing values:", missing_columns)
        
        # Return the correlation matrix
        return correlation_matrix
    except Exception as e:
        print("An error occurred while calculating the correlation matrix:", str(e))
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for the given data. The descriptive statistics include count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values for each column of the data.

    Input:
    data (pandas.DataFrame or array-like): The data for which descriptive statistics are to be calculated.

    Output:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for each column of the data.
                      Rows represent the variables and columns represent the statistics.
    """
    
    try:
        # Check if the input data is a DataFrame
        if not isinstance(data, pd.DataFrame):
            # Try converting data into a DataFrame
            data = pd.DataFrame(data)
        
        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
        
        return stats
    except Exception as e:
        print("An error occurred while calculating descriptive statistics:", str(e))
        return None
    except ValueError as ve:
        print("The input data is not a DataFrame or cannot be converted into a DataFrame.")
        return None