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
    '''Goal: Using pandas module to Calculate Correlation Matrix and descriptive statistics of a given data.
      Function: calculate_correlation(data): 
      - this function takes a pandas dataframe as input and returns covariance matrix of the data. 
      
      Parameters: 
      - data: input data which is used to calculate covariance matrix. 
       
      Returns:
      - correlation)matrix: correlation matrix of the input data. '''
    # Calculate the correlation matrix
    try: 
        correlation_matrix = data.corr()
        return correlation_matrix
    # Return the correlation matrix
    except Exception as e: 
        print(f'An error occured when calculating the correlation matrix:{e}')
        return None
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    '''Goal: Using pandas module and input data to calculate descriptive statistics of the given data
      Function: calculate_descriptive_statistics(data):
      - This function takes the data input and returns the descriptive statistics of the data. 
      
      Parameters: 
      - data: input data which is used to calculate or display the descriptive statistics. 
      
      Returns: 
      - stats: Returns descriptive statistics of the input data.
      '''

    # Calculate descriptive statistics
    try: 
        stats = data.describe(include='all').T
        stats['missing_values'] = data.isnull().sum()
            
        return stats
    except Exception as e: 
        print(f'An error occured when calculating and displaying the descriptive statistics: {e}')
        return None
    


