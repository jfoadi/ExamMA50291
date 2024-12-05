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
    Calculate and return the correlation matrix for a given DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing numerical data for correlation analysis.

    Returns:
        pd.DataFrame: A DataFrame representing the correlation matrix, showing the pairwise correlation 
                      coefficients between the columns.
    
    Notes:
        - The correlation matrix measures the linear relationships between numerical columns.
        - Values close to 1 or -1 indicate a strong positive or negative correlation, respectively.
        - NaN values in the data may affect correlation calculations and should be handled beforehand if necessary.
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")
        
        # Calculate the correlation matrix
        correlation_matrix = data.corr()
        
        # Return the correlation matrix
        return correlation_matrix
    
    except Exception as e:
        print(f"Error calculating correlation matrix: {e}")
        return None

## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Compute and return descriptive statistics for each column in a DataFrame, including missing value counts.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing data to analyze.

    Returns:
        pd.DataFrame: A DataFrame containing descriptive statistics for each column, such as:
                      - Count, mean, standard deviation, min, and max for numerical columns.
                      - Count of unique values, most frequent values (top), and their frequencies for categorical columns.
                      - The number of missing values in each column is added as an extra field.

    Notes:
        - This function uses pandas' `describe()` method, transposes the result for better readability, and adds 
          information about missing values.
        - Useful for an initial exploratory data analysis (EDA) to understand data distribution and completeness.
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")
        
        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
        
        return stats
    
    except Exception as e:
        print(f"Error calculating descriptive statistics: {e}")
        return None
