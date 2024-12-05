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
  