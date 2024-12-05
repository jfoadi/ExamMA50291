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
    raise ImportError("*** ERROR: You do not currently have Pandas installed. Please install it to use this code ***")

## Function to calculate the correlation matrix
def calculate_correlation(data):
    """
    This function computes the correlation between each pair of columns in the provided 
    DataFrame to then calculate the correlation matrix of a given DataFrame. 
    
    Parameters:
        1 > data: The Pandas DataFrame containing the data. 
                  The columns in this DataFrame should be numerical.

    Returns:
        1 > correlation_matrix: a Pandas DataFrame representing the correlation matrix. Each cell in the matrix 
                                contains the correlation coefficient between two columns of the input DataFrame.
    """

    try:
        # CHECK 1: Check to see if the data is a Pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise TypeError("\n*** ERROR: The input data must be a pandas DataFrame. ***")
        
        # CHECK 2: Check to see if the DataFrame is empty
        if data.empty:
            raise ValueError("\n*** ERROR: The input DataFrame is empty. Please provide data. ***")

        # CHECK 3: Check to see if the columns contain only numerical data as required (NaNs are allowed)
        if not all(pd.api.types.is_numeric_dtype(data[col]) for col in data.columns):
            raise ValueError("\n *** ERROR: The DataFrame contains non-numerical column(s). Please provide a DataFrame with numerical data. ***")

        # If the data passes both checks, calculate the correlation matrix
        correlation_matrix = data.corr()

        # Return the correlation matrix
        return correlation_matrix

    except Exception as e:
        print(f"\n*** ERROR: An unexpected error occurred: {e} ***")
        print('\n Please try again, entering only a Pandas DataFrame as the input data.')

    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    This function calculates descriptive statistics for each column in the DataFrame, Iincluding count, mean, 
    standard deviation, min, max, and percentiles (25%, 50%, 75%). Additionally, it calculates the number of missing 
    values for each column.

    Parameters:
        1 > data: The Pandas DataFrame containing the data. 
                  The columns in this DataFrame should be numerical.

    Returns:
        1 > stats: A Pandas DataFrame containing descriptive statistics for each column in 
                   the input DataFrame, including count, mean, std, min, max, and percentiles, 
                   along with the count of missing values for each column.
    
    """
    try:
        # CHECK 1: Check to see if the data is a Pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise TypeError("\n*** ERROR: The input data must be a pandas DataFrame. ***")
        
        # CHECK 2: Check to see if the DataFrame is empty
        if data.empty:
            raise ValueError("\n*** ERROR: The input DataFrame is empty. Please provide data in the DataFrame. ***")

        # CHECK 3: Check to see if the columns contain only numerical data as required (NaNs are allowed)
        if not all(pd.api.types.is_numeric_dtype(data[col]) for col in data.columns):
            raise ValueError("\n *** ERROR: The DataFrame contains non-numerical column(s). Please provide a DataFrame with numerical data. ***")

        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()

        return stats

    except Exception as e:
        print(f"\n*** ERROR: An unexpected error occurred: {e} ***")
        print('\n Please try again, entering only a Pandas DataFrame as the input data.')


