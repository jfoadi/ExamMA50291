# Demo file to showcase visually the joint use of define_dataframe_structure() 
# simulate_data() 


# Importing the created package: Cluster_maker
import cluster_maker as cm 

# importing visualizing library
import matplotlib.pyplot as plt

# Main fucntion
if __name__ == "__main__": 
# Creating input for define_dataframe_structure
    column_specs = [ 
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]

# Using define_data_frame_structure to create a dataframe and printing the data for 
# the user to see structure and output
df = cm.define_dataframe_structure(column_specs)
print("Dataframe structure:")
print(df) 

# Using simualted_data function to simulate and create a dataframe and print the data
# for the user to see structure and output 
data = cm.simulate_data(df, 20)
print("Simulated data:")
print(data)

# Plot size 
plt.figure(figsize =(15, 5))

# Here, plotting the height vs the weight of the data points that we have
plt.subplot(1, 3, 1)
plt.scatter(data['height'], data['weight'], alpha = 0.5)
plt.title('Height vs Weight')
plt.xlabel('Height')
plt.ylabel('Weight')

# Here, plotting the height vs the age of the data points that we have
plt.subplot(1, 3, 2)
plt.scatter(data['height'], data['age'], alpha=0.5)
plt.title('Height vs Age')
plt.xlabel('Height')
plt.ylabel('Age')

# Here, plotting the weight vs the age of the data points that we have
plt.subplot(1, 3, 3)
plt.scatter(data['age'], data['weight'], alpha=0.5)
plt.title('Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')

# Displaying the plots generated
plt.tight_layout()
plt.show()
