###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_correlation(data):
    """
    Calculates the correlation matrix for a given pandas DataFrame.

    This function calculates the pairwise correlation between the numerical columns in the pandas DataFrame. The correlation values 
    range from -1 to 1, where 1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no 
    correlation between the variables.

    Input Parameters:
        data (pd.DataFrame): A pandas DataFrame containing numerical columns for which the correlation matrix needs to be calculated.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the correlation matrix of the input data. Each element in the matrix represents the
        correlation coefficient between the corresponding columns in the input data.

    """
    try:
        # Type check
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")

        # Ensure the DataFrame is not empty
        if data.empty:
            raise ValueError("The DataFrame is empty. Provide a DataFrame with data.")

        # Compute the correlation matrix
        correlation_matrix = data.corr()

        # Handle case where correlation cannot be computed (e.g., all non-numerical data)
        if correlation_matrix.empty:
            raise ValueError("Correlation matrix is empty. Ensure the DataFrame contains numerical columns.")

        return correlation_matrix

    except TypeError as te:
        logging.error(f"TypeError occurred: {te}")
        return {"error": "Invalid input type", "details": str(te)}

    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
        return {"error": "Value error", "details": str(ve)}

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return {"error": "Unexpected error", "details": str(e)}


def calculate_descriptive_statistics(data):
    """
    Calculates the descriptive statistics for a given pandas DataFrame.

    This function computes descriptive statistics such as count, mean, standard deviation, minimum, maximum, 
    and quartiles for each column in the provided pandas DataFrame. Additionally, it calculates the 
    number of missing values for each column.

    Input Parameters: 
        data (pd.DataFrame): A pandas DataFrame containing the data for which descriptive statistics are to be computed.

    Returns:
        pd.DataFrame: A DataFrame containing the descriptive statistics for each column in the input data. The descriptive statistics of each column in the original dataframe 
        is represented as a row in the output DataFrame. The columns of the output DataFrame include 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', and 'missing_values'.

    """
    try:
        # Type check
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")

        # Ensure the DataFrame is not empty
        if data.empty:
            raise ValueError("The DataFrame is empty. Provide a DataFrame with data.")

        # Compute descriptive statistics
        stats = data.describe(include="all").T

        # Add a column for missing values
        stats["missing_values"] = data.isnull().sum()

        return stats

    except TypeError as te:
        logging.error(f"TypeError occurred: {te}")
        return {"error": "Invalid input type", "details": str(te)}

    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
        return {"error": "Value error", "details": str(ve)}

    except KeyError as ke:
        logging.error(f"KeyError occurred: {ke}")
        return {"error": "Key error in DataFrame", "details": str(ke)}

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return {"error": "Unexpected error", "details": str(e)}
