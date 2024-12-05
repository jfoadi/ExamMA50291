###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_exporter.py
###

## Libraries needed
import pandas as pd

## Function to export data to a CSV file
def export_to_csv(data, filename, delimiter=",", include_index=False):
    """
    Export the DataFrame to a CSV file.

    Parameters:
        data (pd.DataFrame): The DataFrame to export.
        filename (str): Name of the output CSV file.
        delimiter (str): Delimiter for the CSV file (default: ',').
        include_index (bool): Whether to include the DataFrame index (default: False).

    Returns:
        None
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("filename must be a non-empty string")
        if not isinstance(delimiter, str) or len(delimiter) != 1:
            raise ValueError("delimiter must be a single character string")
        if not isinstance(include_index, bool):
            raise TypeError("include_index must be a boolean")

        data.to_csv(filename, sep=delimiter, index=include_index)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")


## Function to export data to a formatted text file
def export_formatted(data, filename, include_index=False):
    """
    Exports the DataFrame to a text file with formatted numbers.
    
    Real numbers are formatted as %fw.3 (width depends on the largest number).
    The space between columns is exactly three characters.
    Headers are centered in each column.
    
    Parameters:
    data (pd.DataFrame): The data to export.
    filename (str): The name of the file to export the data to.
    include_index (bool): Whether to include the DataFrame index in the output.
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("filename must be a non-empty string")
        if not isinstance(include_index, bool):
            raise TypeError("include_index must be a boolean")

        # Determine the width for each column
        column_widths = []
        for col in data.columns:
            max_width = max(data[col].apply(lambda x: len(f"{x:.3f}") if isinstance(x, float) else len(str(x))).max(), len(col))
            column_widths.append(max_width)
        
        # Adjust column widths for consistent spacing between columns
        column_widths = [width + 3 for width in column_widths]

        with open(filename, 'w') as file:
            # Write headers
            headers = [f"{col:^{column_widths[i]}}" for i, col in enumerate(data.columns)]
            if include_index:
                index_width = max(len('Index'), len(str(data.index.max()))) + 3
                headers.insert(0, f"{'Index':^{index_width}}")
            file.write("".join(headers) + "\n")
            
            # Write data rows
            for index, row in data.iterrows():
                formatted_row = []
                if include_index:
                    formatted_row.append(f"{index:{index_width}d}")
                for i, item in enumerate(row):
                    if isinstance(item, int):
                        formatted_row.append(f"{item:{column_widths[i]}d}")
                    elif isinstance(item, float):
                        formatted_row.append(f"{item:{column_widths[i]}.3f}")
                    else:
                        formatted_row.append(f"{str(item):{column_widths[i]}}")
                file.write("".join(formatted_row) + "\n")
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to text file: {e}")
    
