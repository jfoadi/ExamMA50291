# Description of Question Answers

# Question 1 

Changed _ to __

# Question 2

Verified function availability, fixed import path

# Question 3

Added docstrings to functions in data_analyser.py

# Question 4

Added exception handling to data_analyser.py

# Quesion 5

Corrected import calculate_correlation

# Question 6

Created the demo_cm.py file

The demo_cm.py file demonstrates how to use the main functions from the cluster_maker package.

define_dataframe_structure()

Creates a DataFrame based on inputted representative values.
simulate_data()

Generates simulated data points around the seed values, using normal or uniform distributions with user-specified variances.
What the Demo Shows:
Histograms with Age Groups:
Each column's histogram is divided by age group. The mean and variance range (mean ± variance) are marked with vertical lines.

Scatter Plot of Groups:
Plots height vs. weight with colors indicating age groups, making it easy to spot patterns.

# Question 7

The intelligent_clusters module includes the function create_separated_clusters(), which generates groups of simulated data that are clearly separated based on a given separation factor. The function either uses an existing seed DataFrame or generates one using column_specs. The separation_factor controls the distance between the group centers, ensuring that the groups are well-distanced from each other. The separation is deterministic, giving you precise control over how separated the groups are.

Visualise_clusters wasn't needed but helped to understand outputs & testing convenience

How to Test create_separated_clusters()
To test this function, run the script test4_cm.py. The script:

Prompts you to input key parameters like feature distributions (normal or uniform), variance, separation factor, and the number of data points per group.
Uses the provided inputs to generate the clusters.
Prints out a sample of the generated data and the distribution of the groups.
Visualizes the data with scatter plots and histograms, color-coded by age.
Steps to Test:
Run the test script:
bash
Copy code
python test4_cm.py
Enter the requested values when prompted.
Check the printed sample data and group distribution.
View the visualizations to see how well-separated the groups are.