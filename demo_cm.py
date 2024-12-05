###
## Demo for visual use of define_dataframe_structure() and simulate_data()
###

# Import libraries
import cluster_maker as cm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Create Input for define_dataframe_structure
    column_specs = [
        {"name": "height", "reps": [180,160,120,100,80,150,170]},
        {"name": "weight", "reps": [70,60,50,45,40,80,90]},
        {"name": "age", "reps": [20,35,30,10,24,43,56]},
    ] 

    # Define the structure of the dataframe 
    df = cm.define_dataframe_structure(column_specs)
    print("Dataframe Created:")
    print(df)

    # Simulate data for the dataframe
    data = cm.simulate_data(df, 20)
    print("Simulated Data:")
    print(data)
       # Scatter plot for Height vs Weight
    plt.subplot(3, 1, 1)
    sns.scatterplot(data=data, x="height", y="weight", color="blue", s=100)
    plt.title("Height vs Weight", fontsize=12)
    plt.xlabel("Height (cm)", fontsize=8)
    plt.ylabel("Weight (kg)", fontsize=8)
    plt.grid(True)

    # Scatter plot for Age vs Weight
    plt.subplot(3, 1, 2)
    sns.scatterplot(data=data, x="age", y="weight", color="orange", s=100)
    plt.title("Age vs Weight", fontsize=12)
    plt.xlabel("Age (years)", fontsize=8)
    plt.ylabel("Weight (kg)", fontsize=8)
    plt.grid(True)

    # Scatter plot for Height vs Age
    plt.subplot(3, 1, 3)
    sns.scatterplot(data=data, x="height", y="age", color="green", s=100)
    plt.title("Height vs Age", fontsize=12)
    plt.xlabel("Height (cm)", fontsize=8)
    plt.ylabel("Age (years)", fontsize=8)
    plt.grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.suptitle("Visualizations of Simulated Data", fontsize=16, y=1.0)

    # Show the plots
    plt.show()


if __name__ == "__main__":
    main()

