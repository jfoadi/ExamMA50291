###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

## Create input for define_dataframe_structure
column_specs = [
    {'name': 'height', 'reps': [180, 160, 120]},
    {'name': 'weight', 'reps': [80, 60, 30]},
    {'name': 'age', 'reps': [40, 35, 10]}
]

df = cm.define_dataframe_structure(column_specs)
print(df)