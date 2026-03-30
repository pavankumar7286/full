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

# Scatter plot
plt.figure(figsize=(12,6))
plt.scatter(years, runs, color="red", marker="o", s=50, label="Runs per Season")

plt.title("Virat Kohli's Runs Over the Years in IPL")
plt.xlabel("Year")
plt.ylabel("Runs")

# Show every year on x-axis
plt.xticks(years, rotation=45)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
