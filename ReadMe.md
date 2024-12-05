# Adam Young 
# 05/12/2024

# Information about the work I have done on the package and test files:

## 1
> I have fixed the file 'test0_cm.py' by changing '._doc_' to '.__doc__'
> This file now retrieves the docstring of the function 'define_dataframe_structure' and prints it for the user when ran
> The file now runs successfully when executed (The package was not changed)

## 2
> The error in the original 'test1_cm.py' was due to the line 51: max_length = max(max_length, len(spec.get('reps', []) - 0) + 1)
> This line tries to subtract 0 from a list, which produces an error 
> To fix this line we change it to: max_length = max(max_length, len(spec.get('reps', [])))
> This line now correctly calculates the maximum length of the list with no errors
> The test file 'test1_cm.py' now runs successfully when executed (The test file was not changed but the package was)

## 3
> I have added appropriate and human-readable docstrings to both of the functions in the file 'data_analyser.py'

## 4
> I have added relevent exception handling to the functions 'calculate_correlation' and calculate_descriptive_statistics 
  in the file 'data_analyser.py'
> Both of the functions take a Pandas DataFrame as an input so can use the same exception handling for both of them
> Now, the function goes though three tests for the DataFrame provided
    > 1: Checks if the Data frame is in the form of a Pandas DataFrame
    > 2: Checks if the DataFrame is empty
    > 3: Checks if the DataFrame contains any non-numeric data
> If any of these tests fail, the function raises an appropriate error message
> If another error occurs during the execution of the function, it is caught and a more generic error message is raised

## 5
> I have modified the file 'test2_cm.py' so it runs successfully (not changed the package)
> Before, the file tried to run the function 'corre1ation_matrix', which does not exist
> However, this did not preduce an error because there was an exeception in the code, stating that if there is an 
  error running this part of the code, that it will pass and continue running the rest of the code
> This means that, the test file is run without errors, however, it does not produce the desired output
> To fix this and print the desired output of the correlation matrix, I have changed corre1ation_matrix to correlation_matrix
> Now, the test file runs successfully and prints the desired output
> I have also improved the user interface on the output to make it look better

## 6
> I have created a demo file named 'demo_cm.py' that does the following:
> Creates a sample DataFrame, showing some marks for different University courses, these are the seed values
> For each course, it simulates the marks for 250 students, given two uniform and one normal distribution
> Visually displays the distribution of the marks for each course on a histogram
> This demo file is a good example of joint use of the 'define_dataframe_structure' and 'simulate_data' functions



