# creating_synthetic_data.py

# this file allows the user to make synthetic data for clustering

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles
from sklearn.metrics import silhouette_score, davies_bouldin_score

def generate_custom_data():
    """
    Generate custom datasets with various geometries and noise levels.
    """
    try:
        print("\nSelect the dataset type:")
        print("1. Blobs (default)")
        print("2. Moons (non-linear)")
        print("3. Circles (non-linear)")

        choice = input("Enter the dataset type (1-3): ").strip()
        n_samples = int(input("Number of data points: ").strip())
        noise = float(input("Noise level (0.0 - 1.0): ").strip())

        if choice == '2':
            data, _ = make_moons(n_samples=n_samples, noise=noise, random_state=42)
        elif choice == '3':
            data, _ = make_circles(n_samples=n_samples, noise=noise, factor=0.5, random_state=42)
        else:
            data, _ = make_blobs(n_samples=n_samples, centers=3, n_features=3, random_state=42)

        return StandardScaler().fit_transform(data)
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def evaluate_clustering(data, labels):
    """
    Evaluate clustering performance using silhouette and Davies-Bouldin scores.
    """
    try:
        silhouette = silhouette_score(data, labels)
        db_index = davies_bouldin_score(data, labels)
        print(f"\nSilhouette Score: {silhouette:.4f}")
        print(f"Davies-Bouldin Index: {db_index:.4f}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")