import matplotlib.pyplot as plt

# Runs data
runs = [
    165, 246, 307, 557, 364, 634, 
    359, 505, 973, 308, 530, 464, 
    466, 405, 341, 639, 741, 731
]

# Histogram
plt.figure(figsize=(10,6))
plt.hist(runs, bins=8, color="skyblue", edgecolor="black")
plt.title("Distribution of Virat Kohli's IPL Runs (2008–2025)")
plt.xlabel("Runs per Season")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
