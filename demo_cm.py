import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cluster_maker as cm

if __name__ =='__main__':
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]}
    ]
    col_specs = {
    'height': {'distribution': 'normal', 'variance': 5.0},
    'weight': {'distribution': 'uniform', 'variance': 10.0}
}
df = cm.define_dataframe_structure(column_specs)
df = df[:-1]
print(df)
#plotting data without simulating the points 
plt.scatter(df['height'],df['weight'])
plt.title("data without adding simulated poiints")
plt.xlabel("height")
plt.ylabel("weight")
plt.show()
data = cm.simulate_data(df,10,col_specs)

#plotting the data after simulating the points
plt.scatter(data['height'],data['weight'])
plt.title("data after adding simulated poiints")
plt.xlabel("height")
plt.ylabel("weight")
print(data)
plt.show()


#this part is to check working of create clusters function in the intelligent clusters module.
simulated_data = cm.create_clusters(data, n_points=50, col_specs=col_specs, separation_factor=30, n_clusters=3)
print(simulated_data)
plt.figure(figsize=(10, 6))
plt.scatter(simulated_data['height'], simulated_data['weight'], alpha=0.6, c='blue', label='Simulated Points')
plt.xlabel("Height")  # Add x-label
plt.ylabel("Weight")  # Add y-label
plt.title("Scatter Plot of Simulated Data") 
plt.grid(True) 
plt.legend()  # Add legend
plt.show()