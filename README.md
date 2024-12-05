
# Test Solution. 

## Declaration of the use of copilot. 
 
I, (Student number: 239716451), used Microsoft Copilot to assist in solving this test. I leveraged Copilot's guidance to generate the code and write the function descriptions for each problem. Additionally, I reviewed and modified the outcomes generated by Copilot to ensure accuracy and relevance.

## General modifications

Three files are added to the repo before starting to solve the test: 
- A directory called `outputs` to store the results of the code.
- README.md document containing some explanations of the code
- A jupyter notebook called Trial_error_notebook.ipynb to chech the performance of the code. 

## Solutions 

1)  Modify the package or the file "test0_cm.py" (not both), to make "test0_cm.py" run successfully. 

The change I made on test0_cm.py was calling the define_dataframe_structure function from the cluster_maker module and printing its documentation string using the __doc__ attribute.


2) Modify the package or the file "test1_cm.py" (not both), to make 
 "test1_cm.py" run successfully.

 I changed the function define_dataframe_structure() in the package cluster_maker/dataframe_builder.py. The change was this:
    - max_length = max(max_length, len(spec.get('reps', [])-0)+1)
    + max_length = max(max_length, len(spec.get('reps', [])))

3) Try and understand what the functions in module "data_analyser.py" do and write an appropriate, human-readable, docstring for each one of them.

There are two function in data_analyser.py. 

- calculate_correlation(data) : Calculates the correlation matrix for the given data.
- calculate_descriptive_statistics(): Calculate descriptive statistics for the given data. The descritive statistics include count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values for each column of the data 
    includes 
    - Count
    - Mean 
    - Standard deviation 
    - Minimum value
    - 25th percentile
    - Median or 50th percentile
    - 75th percentile
    - Maximum value
    - Number of missing values in each column.

4) Add appropriate exception handling to both functions in "data_analyser.py". The exception handling should be effective, informative, and should not crash the program.

Exception handling was added to both functions in data_analyser.py. The exceptions check the type of the input and print informative messages about the reasons of why the fucntion cannot generate the output. 

5) Modify the package or the file "test2_cm.py" (not both), to make 
    "test2_cm.py" run successfully.

I changed the file test2_cm.py and the chanfeg as git shows were : 

     try:
    -    crr = cm.corre1ation_matrix(data)
    +    crr = cm.calculate_correlation(data)
    +    print("The correlation matrix is:")
    +    print(crr)
And 

    - print("Is everything really working?")
    \ No newline at end of file
    + print("Is everything really working? Now everything is working because it is possible to compute the correlation matrix!")


6) Write a demo file, called "demo_cm.py", that demonstrates visually the joint use of define_dataframe_structure() and  simulate_data().

A demo_cm.py was created as a guidilene of the use of the package `cluster_maker`.


7) Add a new function to a new module called "intelligent_clusters.py" that, based on the seed dataframe created by define_dataframe_structure(), and using simulate_data(),
creates groups which are well separated from each other. Among
the input parameters, make sure to include one that describes group separation.

The new module intelligent_clusters.py was added to the library and a demostration was included in the file demo2_cluster_cm.py



## Additional material. 

`Demos descriptions.`

