import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/pavankumar7286/full/refs/heads/main/sales_data.csv"
df = pd.read_csv(url)
df = pd.read_csv(url)

print(df.columns)   # Step 1: check column names
print(df.head())    # Step 2: preview data

# Suppose the column is 'Item' instead of 'Product'
product_sales = df.groupby("Item")["Quantity"].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=product_sales.index, y=product_sales.values, palette="viridis")
plt.title("Total Quantity Sold per Item")
plt.ylabel("Quantity Sold")
plt.xlabel("Item")
plt.show()
