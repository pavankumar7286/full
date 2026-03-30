import matplotlib.pyplot as plt

# Data
years = [
    2008, 2009, 2010, 2011, 2012, 2013, 
    2014, 2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024, 2025
]
runs = [
    165, 246, 307, 557, 364, 634, 
    359, 505, 973, 308, 530, 464, 
    466, 405, 341, 639, 741, 731
]

# Create figure with subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(12,12))

# Line plot
axs[0,0].plot(years, runs, marker='o', color='blue')
axs[0,0].set_title("Line Plot")
axs[0,0].set_xlabel("Year")
axs[0,0].set_ylabel("Runs")
axs[0,0].set_xticks(years)

# Bar plot
axs[0,1].bar(years, runs, color='salmon', edgecolor='black')
axs[0,1].set_title("Bar Plot")
axs[0,1].set_xlabel("Year")
axs[0,1].set_ylabel("Runs")

# Scatter plot
axs[1,0].scatter(years, runs, color='green', s=80)
axs[1,0].set_title("Scatter Plot")
axs[1,0].set_xlabel("Year")
axs[1,0].set_ylabel("Runs")

# Histogram
axs[1,1].hist(runs, bins=8, color='purple', edgecolor='black', alpha=0.7)
axs[1,1].set_title("Histogram of Runs")
axs[1,1].set_xlabel("Runs per Season")
axs[1,1].set_ylabel("Frequency")

# Adjust layout
plt.tight_layout()
plt.show()
