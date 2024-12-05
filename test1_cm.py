###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

## Create input for define_dataframe_structure
column_specs = [
    {'name': "height", 'reps': [180, 160, 120]},
    {'name': "weight", 'reps': [80, 60, 30]},
    {'name': "age", 'reps': [40, 35, 10]}
]

#height = {"height" : [180, 160, 120]}
#weight = {"weight" : [80, 60, 30]}
#age = {"age" : [40,35,10]}
#column_specs = [height, weight, age]

#column_specs = [
#    {"height": [180, 160, 120]},
#    {"weight": [80, 60, 30]},
#    {"age" : [40, 35, 10]}
#]

## Create the dataframe, based on the above info
df = cm.define_dataframe_structure(column_specs)
print(df)
