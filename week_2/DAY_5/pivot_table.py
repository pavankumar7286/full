import pandas as pd
# Step 1: Create sample dataset
data = {
    "OrderID": [1,2,3,4,5,6,7,8],
    "Region": ["North","South","East","West","North","South","East","West"],
    "ProductCategory": ["Electronics","Furniture","Electronics","Clothing",
                        "Furniture","Clothing","Electronics","Furniture"],
    "Sales": [1200,800,1500,600,700,400,900,1100],
    "Year": [2024,2024,2025,2025,2024,2025,2025,2024]  # Added Year column
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)
# Step 2: Pivot table (Sales per Region/Year)
pivot = pd.pivot_table(df,
                       values="Sales",
                       index="Region",   # rows
                       columns="Year",   # columns
                       aggfunc="sum",    # aggregation
                       fill_value=0,     # replace NaN with 0
                       margins=True)     # include grand totals

print("\nPivot Table (Sales per Region and Year):\n", pivot)
