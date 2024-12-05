import pandas as pd
from cluster_maker import data_analyser as da

def test_calcualte_correlation():
    print("Testing calculate_correlation function ...\n")

    # Test with invalid input(not a DataFrame)
    print("Test 1: Invalid input (not a DataFrame)")
    result = da.calculate_correlation("not a dataframe")
    print(f"Result: {result}\n")

    # Test with empty DataFrame
    print("Test 2: Empty DataFrame")
    empty_df = pd.DataFrame()
    result = da.calculate_correlation(empty_df)
    print(f"Result: {result}\n")

    # Test with valid DataFrame
    print("Test 3: valid DataFrame")
    valid_df = pd.DataFrame({
        'A': [1, 2, 3], 
        'B': [4, 5, 6]
    })
    result = da.calculate_correlation(valid_df)
    print(f"Result: {result}\n")



def test_calculate_descriptive_statistics():
    print("Testing calculate_descriptive_staatistics sunction ...\n")

    # Test with invalid input(not a DataFrame)
    print("Test 1: Invlaid input (not a DataFrame)")
    result = da.calculate_descriptive_statistics("not a dataframe")
    print(f"Result: {result}\n")

    # Test with empty DataFrame
    print("Test 2: Empty DataFrame")
    empty_df = pd.DataFrame()
    result = da.calculate_descriptive_statistics(empty_df)
    print(f"Result: {result}\n")

    # Test with valid DataFrame
    print("Test 3: valid DataFrame")
    valid_df = pd.DataFrame({
        'A': [1, 2, 3], 
        'B': [4, 5, 6]
    })
    result = da.calculate_descriptive_statistics(valid_df)
    print(f"Result: {result}\n")



def run_tests():
    test_calcualte_correlation()
    test_calculate_descriptive_statistics()

if __name__ == "__main__":
    run_tests()


