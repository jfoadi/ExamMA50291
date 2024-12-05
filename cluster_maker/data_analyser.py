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
    '''Goal: Using pandas library to Calculate Correlation Matrix of a given data.
      Function: calculate_correlation(data): 
      - this function takes a pandas dataframe as input and returns the covariance matrix of the data. 
      
      Parameters: 
      - data: input data which is used to calculate covariance matrix. 
       
      Returns:
      - correlation_matrix: correlation matrix of the input data. '''
    # Calculate the correlation matrix (with included excpetion handling)
    try: 
        if not isinstance(data, pd.DataFrame):
            raise TypeError('Input data must be a pandas DataFrame')
        correlation_matrix = data.corr()
        return correlation_matrix
    # Return the correlation matrix
    except (ValueError, TypeError) as e: 
        print(f'An error occured when calculating the correlation matrix:{e}')
        return None
    except Exception as e: 
        print('An unexcpected error occured: {e}')
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    '''Goal: Using pandas library and input data to calculate descriptive statistics of the given data.
      Function: calculate_descriptive_statistics(data):
      - This function takes the data input and returns the descriptive statistics of the data. 
      
      Parameters: 
      - data: input data which is used to calculate and display the descriptive statistics. 
      
      Returns: 
      - stats: Returns descriptive statistics of the input data.
      '''

    # Calculate descriptive statistics (with included exception handling)
    try: 
        if not isinstance(data, pd.DataFrame):
            raise TypeError('Input data must be a pandas DataFrame')
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
        return stats
    except (ValueError, TypeError) as e: 
        print(f'An erro occured when calculating the descriptive statistics: {e}')
        return None
    except Exception as e: 
        print(f'An unexpected error occured: {e}')
        return None
    


