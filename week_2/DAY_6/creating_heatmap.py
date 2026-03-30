import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data
years = [
    2008, 2009, 2010, 2011, 2012, 2013, 
    2014, 2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024, 2025
]
runs = [
    165, 246, 307, 557, 364, 634, 
    359, 505, 973, 308, 530, 464, 
    466, 405, 341, 639, 741, 657
]

# Convert to DataFrame
df = pd.DataFrame({'Year': years, 'Runs': runs})

# Pivot for heatmap
df_pivot = df.pivot_table(index='Year', values='Runs')

# Heatmap
plt.figure(figsize=(6,8))
sns.heatmap(df_pivot, annot=True, cmap='coolwarm', fmt='g')  # fixed fmt

plt.title("Virat Kohli's IPL Runs Heatmap (2008–2025)")
plt.ylabel("Year")
plt.xlabel("Runs")
plt.show()
