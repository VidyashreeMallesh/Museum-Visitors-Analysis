# This code gives the graph of Chinese American Museum on annual basis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
museum_filepath = "museum-visitors.csv"
museum_data = pd.read_csv("museum-visitors.csv", index_col="Month", parse_dates=True)
museum_data.head()
museum_data = museum_data[['Avila Adobe', 'Chinese American Museum', 'Firehouse Museum', 'America Tropical Interpretive Center']]
plt.figure(figsize=(8,4))
plt.title("Monthly / Annual Visitors to Chinese American Museum")
sns.lineplot(data=museum_data['Chinese American Museum'])
plt.xlabel("Date")