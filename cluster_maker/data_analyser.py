###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries

try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. Some functions may not work.")
## Function to calculate the correlation matrix
def calculate_correlation(data):
    """
    Calculate the correlation matrix for a given DataFrame.

    Parameters:
        data (pd.DataFrame): A pandas DataFrame containing numerical columns for which the correlation matrix will be calculated.

    Returns:
        pd.DataFrame: A DataFrame representing the correlation matrix of the input data.
    """

    try:
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")

        correlation_matrix = data.corr()
        if correlation_matrix.empty:
            raise ValueError("The DataFrame contains no numerical data to compute correlations.")

        return correlation_matrix
    except Exception as e:
        print(f"Error calculating correlation matrix: {e}")
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for a given DataFrame, including summary statistics and missing values.

    Parameters:
        data (pd.DataFrame): A pandas DataFrame for which descriptive statistics will be calculated.

    Returns:
        pd.DataFrame: A transposed DataFrame containing descriptive statistics (e.g., count, mean, std, min, max, etc.)
                      for each column in the input data, along with the number of missing values.
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        
        if data.empty:
            raise ValueError("The input DataFrame is empty and contains no data for analysis.")

        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()

        return stats
    except Exception as e:
        print(f"Error calculating descriptive statistics: {e}")
        return None