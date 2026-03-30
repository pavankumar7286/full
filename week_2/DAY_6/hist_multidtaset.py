import matplotlib.pyplot as plt

# Example datasets (runs in different ranges)
dataset1 = [165, 246, 307, 557, 364, 634, 359, 505, 973, 308, 530, 464, 466, 405, 341, 639, 741, 731]
dataset2 = [150, 200, 250, 400, 350, 600, 370, 480, 950, 320, 520, 450, 470, 420, 360, 620, 700, 720]
dataset3 = [180, 260, 310, 540, 370, 620, 340, 490, 960, 300, 510, 460, 480, 410, 350, 630, 710, 740]

# Plot histogram with multiple datasets
plt.figure(figsize=(10,6))
plt.hist(dataset1, bins=10, alpha=0.5, label="Dataset 1", color="blue", edgecolor="black")
plt.hist(dataset2, bins=10, alpha=0.5, label="Dataset 2", color="green", edgecolor="black")
plt.hist(dataset3, bins=10, alpha=0.5, label="Dataset 3", color="red", edgecolor="black")

plt.title("Overlayed Histogram of Multiple Datasets")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
