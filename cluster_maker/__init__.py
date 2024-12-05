###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
###

## Make functions available to the user 
from .dataframe_builder import (
    define_dataframe_structure,
    simulate_data
)

from .data_exporter import (
    export_to_csv,
    export_formatted
)

from .data_analyser import (
    calculate_correlation,
    calculate_descriptive_statistics
)
from .plot_clusters import plot_clusters

from .intelligent_clusters import intelligent_cluster_groups

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt