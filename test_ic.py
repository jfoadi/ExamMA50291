import intelligent_clusters as ic
import cluster_maker as cm

#Test functionality of intelligent_clusters
column_specs = [
    {'name':'x', 'reps':[2,8]},
    {'name':'y', 'reps':[2,8]}
]

df = cm.define_dataframe_structure(column_specs)
sim_data = ic.create_intelligent_clusters(df, 1, 5)
print(sim_data)