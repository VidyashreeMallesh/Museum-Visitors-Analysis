# This code gives the graph of all the four museum-visitors flow on annual basis

import pandas as pd
import numpy as np
museum_filepath = "museum-visitors.csv"
museum_data = pd.read_csv("museum-visitors.csv", index_col="Month", parse_dates=True)
museum_data.head()
museum_data = museum_data[['Avila Adobe', 'Chinese American Museum', 'Firehouse Museum', 'America Tropical Interpretive Center']]
museum_data.plot()