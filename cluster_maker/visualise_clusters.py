import matplotlib.pyplot as plt
import numpy as np

def visualise_clusters(simulated_data, col_specs):
    """
    Visualising the generated clusters, including scatter plot of the groups and histograms for each feature.
    Highlights key statistical points (mean, variance).

    Arguments:
        simulated_data (pd.DataFrame): The simulated data containing the generated clusters.
        col_specs (dict): The column specifications used for generating the data, containing distribution and variance information.
    """
    # Scatter Plot: Show height vs weight with color coding by group
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        simulated_data['height'], simulated_data['weight'], c=simulated_data['group'], cmap='viridis', alpha=0.7
    )
    plt.colorbar(scatter, label='Group')
    plt.title("Scatter Plot of Height vs Weight by Group")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()

    # Create histograms for each feature (height, weight, age)
    for feature in ['height', 'weight', 'age']:
        plt.figure(figsize=(10, 6))

        # Plot histogram for the feature
        plt.hist(simulated_data[feature], bins=20, alpha=0.7, color='blue', label=feature)
        
        # Get the mean and variance
        mean = simulated_data[feature].mean()
        variance = simulated_data[feature].var()

        # Mark mean and variance on the plot
        plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f"Mean: {mean:.2f}")
        plt.axvline(mean - np.sqrt(variance), color='green', linestyle='dashed', linewidth=2, label=f"Mean - 1 SD")
        plt.axvline(mean + np.sqrt(variance), color='green', linestyle='dashed', linewidth=2, label=f"Mean + 1 SD")
        
        plt.title(f"Histogram of {feature.capitalize()}")
        plt.xlabel(f"{feature.capitalize()}")
        plt.ylabel("Frequency")
        plt.legend()
        plt.grid(True)
        plt.show()