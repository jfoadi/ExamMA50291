## 6) Write a demo file, called "demo_cm.py", that demonstrates
## visually the joint use of define_dataframe_structure() and 
## simulate_data().

# Import cluster_maker
import cluster_maker as cm

# Import useful libraries
import matplotlib.pyplot as plt
import pandas as pd

# Example to demonstrate the use of the simulate_data function, using the define_dataframe_structure output as input
print("Example to demonstrate the use of the simulate_data function, using the define_dataframe_structure output as input\n")
data = [{
    'name':'age', 'reps': [25, 30, 35]},
    {'name': 'income', 'reps': [50000, 60000, 70000]
}]

seed_df = cm.define_dataframe_structure(data)

print(f'Seed data frame from define_dataframe_structure function:\n{seed_df}')

# Plot the seed data frame
plt.plot(seed_df['age'], seed_df['income'], 'o')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Seed Data Frame')
plt.grid(True)
plt.show()



# Example col_specs
col_specs = {
    'age': {
        'distribution': 'normal',
        'variance': 4.0
    },
    'income': {
        'distribution': 'uniform',
        'variance': 5.0
    }}

new_df = cm.simulate_data(seed_df, n_points=10, col_specs=col_specs)

print(f'Data frame after simulate_data function:\n{new_df}')

# Plot the new data frame
plt.scatter(new_df['age'], new_df['income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Simulated Data Frame')
plt.grid(True)
plt.show()




## Example to demonstrate the use of intelligent_clusters function
print("\nExample to demonstrate the use of intelligent_clusters function\n")
data = [{
    'name': 'sales', 'reps': [160, 170, 180]},
    {'name': 'profit', 'reps': [60, 70, 80]
}]

seed_df = cm.define_dataframe_structure(data)

separation = 5
col_specs = {
    'sales': {
        'distribution': 'normal',
        'variance': 4.0
    },
    'profit': {
        'distribution': 'uniform',
        'variance': 5.0
    }
}
n_groups = 3
n_points = 100

separated_groups = cm.sepatared_groups(seed_df, separation,col_specs,n_groups,n_points)
print(separated_groups)


import matplotlib.pyplot as plt

plt.scatter(separated_groups['sales'], separated_groups['profit'])
plt.xlabel('Sales compared to last year')
plt.ylabel('Profit this year')
plt.title('Separated Groups')
plt.grid(True)
plt.show()