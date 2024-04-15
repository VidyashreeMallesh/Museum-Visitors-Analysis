# This code gives the frequency of Avila Adobe Museum in histogram 

import pandas as pd
import matplotlib.pyplot as plt
museum_filepath = "museum-visitors.csv"
museum_data = pd.read_csv("museum-visitors.csv", index_col="Month", parse_dates=True)
museum_data.head()
museum_data = museum_data[['Avila Adobe', 'Chinese American Museum', 'Firehouse Museum', 'America Tropical Interpretive Center']]
plt.title("Avila Adobe histogram")
museum_data['Avila Adobe'].plot(kind='hist'); 