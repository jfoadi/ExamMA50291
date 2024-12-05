## 6) Write a demo file, called "demo_cm.py", that demonstrates
## visually the joint use of define_dataframe_structure() and 
## simulate_data().

# Import cluster_maker
import cluster_maker as cm

# Import plotting tools
import matplotlib.pyplot as plt

# Example to demonstrate the use of the simulate_data function, using the define_dataframe_structure output as input
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