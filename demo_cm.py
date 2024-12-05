###
## Demo file
## Student 249290349 - University of Bath - 2024
###

## Import modules (aware some of these are redundant)
import numpy as np
import matplotlib.pyplot as plt
import cluster_maker as cm
import cluster_maker.data_analyser as da

## Main

if __name__ == '__main__':
    try:
        # Create input for define_dataframe_structure
        column_specs = [
            {'name': 'Orbital Radius (10^6km)', 'reps': [57.9, 108.2, 149.6, 228, 778.5, 1432, 2867, 4515]},
            {'name': 'Orbital Period (days)', 'reps': [88, 224.7, 365.2, 687, 4331, 10747, 30589, 59800]},
            {'name': 'Mass (10^24kg)', 'reps': [0.33, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102]}
        ]
        col_specs = {
            'Orbital Radius (10^6km)': {'distribution': 'normal', 'variance': 10.0},
            'Mass (10^24kg)': {'distribution': 'normal', 'variance': 0.2},
            }

        # Create the dataframe, based on the above info
        df = cm.define_dataframe_structure(column_specs)
        print(df)

        # Simulate 5 data points per group, as to emulate measurement uncertainties on planet mass and orbital radius.

        data = cm.simulate_data(df, 5, col_specs)
        crr = da.calculate_correlation(data)
        print(crr)
        matrix = crr.to_numpy()

        #Scatter plotting:

        #plt.scatter(data['Mass (10^24kg)'], data['Orbital Radius (10^6km)'])
        #plt.title("Planet Mass vs Orbital Radius, Correlation = "+ '{0:.3f}'.format(matrix[0,2]))
        #plt.savefig("Mass_vs_OrbRadius.png")
        #plt.close

        plt.scatter(data['Orbital Period (days)'], data['Orbital Radius (10^6km)'])
        plt.title("Orbital Period vs Orbital Radius, Correlation = "+ '{0:.3f}'.format(matrix[0,1]))
        plt.savefig("OrbPeriod_vs_OrbRadius.png")
        plt.close
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")