import cluster_maker as cm
from cluster_maker import intelligent_clusters
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_clusters(data):
    # Set the style for seaborn
    sns.set(style="whitegrid")

    # Create a scatter plot for the clustered data
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=data, x="height", y="weight", hue="group", palette="deep", s=100, alpha=0.9)

    # Add titles and labels
    plt.title("Cluster Visualization: Height vs Weight", fontsize=16)
    plt.xlabel("Height (cm)", fontsize=14)
    plt.ylabel("Weight (kg)", fontsize=14)
    plt.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    # Create Input for define_dataframe_structure
    column_specs = [
        {"name": "height", "reps": [180, 160, 120, 100, 80, 150, 170]},
        {"name": "weight", "reps": [70, 60, 50, 45, 40, 80, 90]},
        {"name": "age", "reps": [20, 35, 30, 10, 24, 43, 56]},
    ] 

    # Define the structure of the dataframe 
    seed_df = cm.define_dataframe_structure(column_specs)

    # Create well-separated clusters
    num_groups = 3
    samples_per_group = 20
    separation = 1  # Adjust this value for more or less separation
    clustered_data = intelligent_clusters.create_intelligent_clusters(seed_df, num_groups, samples_per_group, separation)

    print("Generated Clustered Data:")
    print(clustered_data)

    visualize_clusters(clustered_data)

if __name__ == "__main__":
    main()