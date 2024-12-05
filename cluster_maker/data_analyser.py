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
    Calculate the correlation coefficient for an input dataframe

    The correlation matrix is a table with each dimension the same as the number of 
    variables - where all the variables are somewhat dependent. The entries show the 
    correlation coefficient between the variables. The values in these entries
    are between -1 and 1 where values close to -1 represent strong negative correlation
    and values close to 1 represent strong positive correlation. Value fo 0 
    represents no correlation. 

    Parameters: 
        data (pd.DataFrame) : data is inputed as a pandas DataFrame in a numeric format

    Returns:
        correlation_matrix (pd.DataFrame) : an output DataFrame containing the correlation
                        coefficients of the input data

    
    This function will return a ValueError if there are no numeric columns in the data or if it is emmpty.
    
    """

    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Please input a Pandas DataFrame.")
        if data.empty:
            raise ValueError("Please input a non-empty DataFrame")
        if data.select_dtypes(include=['number']).empty:
            raise ValueError("Please ensure the input DataFrame contrains numeric columns")
        # Calculate the correlation matrix
        correlation_matrix = data.corr()

        # Return the correlation matrix
        return correlation_matrix
    

    except(TypeError, ValueError) as error:
        print(f"Unable to calcuate correlation coefficients due to {error}")
        return None
    except(Exception) as error:
        print(f"Unable to calculate correlation coefficient due to an unidentified error: {error}")
        return None
    

    
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate statistical metrics for an input dataframe

    This provided a statistical description of the columns of the
    input DataFrame of all data types including numerical and categorical. 
    The statistical metrics calculated include count, mean, standard deviation, 
    minimum, maximum and quantiles for numerical data and count, number of
    unique values, mode and frequency of the mode for categorical data. 
    The function also addresses the number of missing values in each column.

    Parameters: 
        data (pd.DataFrame) : data is inputed as a pandas DataFrame
    
    Returns:
        stats (pd.DataFrame) : an output DataFrame with statistical metrics for 
                        columns of data as well as number of missing values for each column.

    This function will return a ValueError if data is empty.

    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Please input a Pandas DataFrame.")
        if data.empty:
            raise ValueError("Please input a non-empty DataFrame")
        if data.select_dtypes(include=['number']).empty:
            raise ValueError("Please ensure the input DataFrame contrains numeric columns")
        # Calculate descriptive statistics
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()

        return stats
    except(TypeError, ValueError) as error:
        print(f"Unable to provide statistical information due to {error}")
        return None
    except(Exception) as error:
        print(f"Unable to provide statistical information due to an unidentified error: {error}")
        return None
    