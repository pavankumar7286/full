import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 6]
# y = [85.12,69.33,87.33,81,85,88.5]
# plt.plot(x, y, marker='o', linestyle='-', color='b')
# plt.title("Pavan's Academic Performance over the years")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid()
# plt.show()

#lineplot
# plt.plot([1,2,3],[10,20,30], label='Line 1', marker='o')
# plt.legend()
# plt.show()

#barchart
# plt.bar(["sslc", "plus one", "plus two", "1sem", "2sem", "3sem"], [85.12, 69.33, 87.33, 81, 85, 88.5], label="Bar Chart", color='skyblue')
# plt.legend()
# plt.show()

#histogram

# # Data
# scores = [85.12, 69.33, 87.33, 81, 85, 88.5]
# # Histogram
# plt.hist(scores, bins=5, color='lightgreen', edgecolor='black')
# plt.title("Pavan's Academic Performance Distribution")
# plt.xlabel("Performance")
# plt.ylabel("Frequency")
# plt.show()

#scatterplot
x = [1, 2, 3, 4, 5, 6]
y = [85.12,69.33,87.33,81,85,88.5]
plt.scatter(x,y, color="red",marker='x')
plt.title("Pavan's Academic Performance over the years")
plt.show()