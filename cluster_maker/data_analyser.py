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

    The function calculates the correlation matrix when a DataFrame is provided

    There is 1 paramete (data) which is a pandas DataFrame

    The function returns a DataFrame of the correlation matrix corresponding to the input data

    """
    try:
        # Checking that data provided is a dataframe.
        if not isinstance(data, pd.DataFrame):
            raise TypeError("The input provided is not a DataFrame")
        # Checking that the data is not empty
        if data.empty:
            raise ValueError("The Data has no numerical data")
        
        # Calculate the correlation matrix
        correlation_matrix = data.corr()
        
        # Return the correlation matrix
        return correlation_matrix

    except TypeError as e:
        print(f"Error calculating correlation: {e}")
        return None
    except ValueError as e: 
        print(f"Error calculating correlation: {e}")
        return None
    except Exception as e:
        print(f"There was an unexpected error: {e}")
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """

    This function is uses a DataFrame as input and returns some statistics related to the Data

    The only parameter is the DataFrame provided (data)

    The function returns the statistics as a dataframe.
    The measures included are count, mean, std, min, 25%, 50%, 75%, max and the count of missing values


    """
    try:
        # Check that data provided is a dataframe
        if not isinstance(data, pd.DataFrame):
            raise TypeError("The input provided is not a DataFrame")
        # Check that the data is not empty
        if data.empty:
            raise ValueError("The Data has no numerical data")
        
        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
            
        return stats
    
    except TypeError as e:
        print(f"Error calculating statistics: {e}")
        return None
    except ValueError as e: 
        print(f"Error calculating statistics: {e}")
        return None
    except Exception as e:
        print(f"There was an unexpected error: {e}")
        return None