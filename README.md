Please run the two files 'demo_cm.py' and 'demo_clustering.py' which are user friendly and below explains what they do.
Then feel free to look through the 'cluster_maker' package.


# Cluster Maker Demo

## Overview
This repository demonstrates the functionality of the `cluster_maker` package, which includes methods for:
- Creating structured DataFrames with custom column specifications.
- Simulating data based on existing DataFrames.
- Performing data analysis such as calculating correlation matrices and descriptive statistics.

The demo file, `demo_cm.py`, provides an interactive user interface to explore these functionalities.

## Features
- **Default DataFrame Creation**: Create a DataFrame with predefined columns (`height`, `weight`, `age`) and view it with descriptive statistics.
- **Simulated Data**: Simulate additional data points based on the existing DataFrame and analyze the results using correlation matrices.
- **Custom DataFrame Creation**: Allow users to create their own DataFrame by specifying columns and representative values, and then analyze the data.
- **Descriptive Statistics**: Calculate summary statistics (count, mean, standard deviation, etc.) for each column in the DataFrame.
- **Correlation Matrix**: Compute and display a correlation matrix showing the relationships between numerical columns.

## Installation

### Prerequisites
Make sure you have Python 3.x installed along with the following dependencies:
- `pandas`
- `prettytable`

You can install the required dependencies by running:

```bash
pip install pandas prettytable

### Example output:

Welcome to the Cluster Maker Demo!
This demo showcases the creation of a structured DataFrame, simulated data, and additional analyses.

Enter '1' to create a default DataFrame, '2' to simulate data, '3' for a custom DataFrame, 'exit' to quit: 1

DataFrame:
+---------+--------+-----+
| height  | weight | age |
+---------+--------+-----+
| 180.0   | 80.0   | 40.0|
| 160.0   | 60.0   | 35.0|
| 120.0   | 30.0   | 10.0|
+---------+--------+-----+

Descriptive Statistics:
+-------------------+------------------+------------------+-----------------+
| Statistic         | height           | weight           | age             |
+-------------------+------------------+------------------+-----------------+
| count             | 3.0              | 3.0              | 3.0             |
| mean              | 160.0            | 56.67            | 28.33           |
| std               | 30.0             | 25.88            | 15.0            |
| min               | 120.0            | 30.0             | 10.0            |
| 25%               | 140.0            | 45.0             | 22.5            |
| 50%               | 160.0            | 60.0             | 35.0            |
| 75%               | 170.0            | 70.0             | 37.5            |
| max               | 180.0            | 80.0             | 40.0            |
| missing_values    | 0.0              | 0.0              | 0.0             |
+-------------------+------------------+------------------+-----------------+

Enter '1' to create a default DataFrame, '2' to simulate data, '3' for a custom DataFrame, 'exit' to quit: 2

Enter the number of data points to simulate per representative: 5

Simulated Data:
+---------+--------+-----+
| height  | weight | age |
+---------+--------+-----+
| 180.0   | 80.0   | 40.0|
| 160.0   | 60.0   | 35.0|
| 120.0   | 30.0   | 10.0|
| 180.0   | 80.0   | 40.0|
| 160.0   | 60.0   | 35.0|
| 120.0   | 30.0   | 10.0|
+---------+--------+-----+

Correlation Matrix:
+---------+---------+---------+-----+
|         | height  | weight  | age |
+---------+---------+---------+-----+
| height  | 1.00    | 0.99    | 0.99 |
| weight  | 0.99    | 1.00    | 1.00 |
| age     | 0.99    | 1.00    | 1.00 |
+---------+---------+---------+-----+





# Clustering Demo

## Overview

This Python script demonstrates the use of various clustering algorithms, showcasing their functionalities using a custom package called `cluster_maker`. It allows the user to simulate data, perform clustering, and view the resulting clusters and statistics. The available clustering algorithms include:

- K-Means
- Affinity Propagation
- Mean-Shift
- Spectral Clustering
- Ward Hierarchical Clustering
- Agglomerative Clustering
- DBSCAN
- OPTICS
- Gaussian Mixture Models (GMM)
- Birch

## Functionality

The demo enables users to:

1. **View Available Clustering Algorithms**: Lists different clustering algorithms along with their parameters, scalability, and use cases.
2. **Create Default DataFrame**: Generates a predefined DataFrame with sample data (height, weight, age) for clustering.
3. **Simulate Custom Data and Perform Clustering**: Allows the user to simulate data based on specified parameters (number of data points, separation factor for clusters) and then apply a chosen clustering algorithm.
4. **Create Custom DataFrame**: Users can define their own DataFrame by specifying column names and values.
5. **Apply Clustering on Existing DataFrame**: Perform clustering on an existing DataFrame using one of the available algorithms.

## Libraries Used

The script relies on the following libraries:

- `cluster_maker`: A custom package containing various clustering algorithms.
- `pandas`: For handling DataFrame operations.
- `prettytable`: To display data and results in a formatted table.
- `numpy`: For numerical operations and handling array-based results.

## How to Run the Demo

The demo is named "demo_clustering.py" simply running this script will allow the user to see all aspects of the program. 