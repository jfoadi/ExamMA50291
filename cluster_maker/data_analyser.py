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
    Creates a correlation matrix for the dataset to show how columns relate to each other.

    This function calculates correlation coefficients for all pairs of columns 
    in your dataset. The results range between -1 and 1:
        - 1 means a strong positive linear relationship.
        - -1 means a strong negative linear relationship.
        - 0 means there is no linear relationship.

    Parameters:
        data (pd.DataFrame): A DataFrame containing numerical data where each 
                             column is treated as a variable.

    Returns:
        pd.DataFrame: A symmetric matrix where each entry (i, j) is the correlation 
                      between column i and column j. The diagonal is always 1 since 
                      each column is perfectly correlated with itself.
    """
    try:
        # Validate input type
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")

        # Check if there are numerical columns
        if data.select_dtypes(include='number').empty:
            raise ValueError("The DataFrame has no numerical columns to calculate correlations.")

        # Calculate the correlation matrix
        correlation_matrix = data.corr()
        return correlation_matrix
    except TypeError as te:
        print(f"TypeError in calculate_correlation: {te}")
        return None
    except ValueError as ve:
        print(f"ValueError in calculate_correlation: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error in calculate_correlation: {e}")
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Breaks down the dataset column by column to give a summary of the key stats.

    This function calculates useful metrics for each column, like the count, mean, 
    standard deviation, min, max, and quartiles for numerical data. For categorical 
    data, it shows things like how many unique values there are, the most common value, 
    and its frequency. It also adds a column for missing values so you can easily see 
    where data is incomplete.

    Parameters:
        data (pd.DataFrame): A DataFrame with your dataset, which can include 
                             numerical or categorical columns.

    Returns:
        pd.DataFrame: A DataFrame where each row corresponds to one of the original 
                      columns in your dataset. The stats include:
                        - Summary for numbers (mean, min, max, etc.)
                        - Summary for categories (unique values, most frequent value)
                        - 'missing_values': Counts how many null entries are in each column.
    """
    try:
        # Validate input type
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")

        # Handle edge case for empty DataFrame
        if data.empty:
            raise ValueError("The DataFrame is empty so can't be analyzed.")

        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
        return stats
    except TypeError as te:
        print(f"TypeError in calculate_descriptive_statistics: {te}")
        return None
    except ValueError as ve:
        print(f"ValueError in calculate_descriptive_statistics: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error in calculate_descriptive_statistics: {e}")
        return None