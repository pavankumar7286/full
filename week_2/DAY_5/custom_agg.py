import pandas as pd
import numpy as np

# -----------------------------
# Step 1: Create sample dataset
# -----------------------------
data = {
    "OrderID": [1,2,3,4,5,6,7,8],
    "Region": ["North","South","East","West","North","South","East","West"],
    "ProductCategory": ["Electronics","Furniture","Electronics","Clothing",
                        "Furniture","Clothing","Electronics","Furniture"],
    "Sales": [1200,800,1500,600,700,400,900,1100],
    "Year": [2024,2024,2025,2025,2024,2025,2025,2024]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

# ------------------------------------------------
# Step 2: Define custom aggregation (variance calc)
# ------------------------------------------------
def variance(x):
    return np.var(x, ddof=1)   # sample variance (ddof=1)

# ------------------------------------------------
# Step 3: Pivot table with multiple aggfuncs
# ------------------------------------------------
pivot_multi = pd.pivot_table(df,
                             values="Sales",
                             index="Region",
                             columns="Year",
                             aggfunc=[np.sum, variance],  # <-- list of functions
                             fill_value=0)

print("\nPivot Table (Sum and Variance of Sales per Region and Year):\n", pivot_multi)
