# Import necessary libraries

try:
    import matplotlib.pyplot as plt
    import cluster_maker as cm 
    import NewModule as nm
except ImportError as e:
    print(f"Error importing required libraries: {e}")
"""
did we need sklearn?
"""
# Main function to run the demo
def main():

    print("Hello, this is a demo of the cluster_maker package.")
    print("I am going to use the same demo data that was provided in test 2")
    print("As we can see this original data is very sparce and we want to padd it out a bit")

    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    
    # Create the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)

    print("This is the dataframe we created:")
    print(df)
    print("")

    example_plot(df,"Original Points")
    plt.show()
    
    print("\nWe can add simulated data to this to make it more dense")
    print("This simulated data is going to have a user defined specific distribuiton arround our original data points")
    print("As we can see in the graph below i have added 200 points to each of the original data points with a rather large variance")

    c_s= {
                'height': {'distribution': 'normal', 'variance': 10.0},
                'weight': {'distribution': 'uniform', 'variance': 10.0},
                'age': {'distribution': 'normal', 'variance': 10.0}
            }
    
    print("This is the distribution we are going to use:")
    print(c_s)

    data = cm.simulate_data(df, 200,col_specs=c_s)
    
    example_plot(data,"Simulated Data")
    plt.show()

    print("\nThis creates issues though as the original data is well seperated but our simulated data is not")
    print("we can solve this by creating a function which contsrains out original simulation distribuion to only create well seperated data")
    print("As you can see, even though we are using the same distribution as before, the data is now well seperated")
    print("Please check my intelligent_cluster.py file for more info about why they look like this")
    data2=(nm.create_well_separated_clusters(df, 20, col_specs=c_s, separation=2, random_state=42))


    example_plot(data2,"Well Seperated Simulated Data")

    plt.show()
    
def example_plot(df,title,same_dims=False):
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')

    ax.scatter(df.height, df.weight, df.age)

    # Labels
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Age')
    
    #set the axis to be the same length
    if same_dims:
        ax.set_box_aspect([1,1,1])
        min_val = df.min().min()
        max_val = df.max().max()
        ax.set_xlim(min_val-max_val/20, max_val+max_val/20)
        ax.set_ylim(min_val-max_val/20, max_val+max_val/20)
        ax.set_zlim(min_val-max_val/20, max_val+max_val/20)

    plt.title(title)
    #plt.show()
if __name__ == '__main__':
    main()
