# Suppose the column is 'Item' instead of 'Product'
# product_sales = df.groupby("Item")["Quantity"].sum()

# plt.figure(figsize=(8,5))
# sns.barplot(x=product_sales.index, y=product_sales.values, palette="viridis")
# plt.title("Total Quantity Sold per Item")
# plt.ylabel("Quantity Sold")
# plt.xlabel("Item")
# plt.show()
