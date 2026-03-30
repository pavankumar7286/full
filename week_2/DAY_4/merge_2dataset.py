import pandas as pd
import numpy as np

df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alex","john","ben"],
    "Age":[25,30,35]
})
df2=pd.DataFrame({
    "ID":[1,2,3],
    "Phy":[87,99,89],
    "Math":[67,73,77],
    "Kannada":[81,76,55]
})
print("Dataset 1: \n",df1)
print("Dataset 2: \n",df2)

merged = pd.merge(df1,df2)
# print("merged dataset: \n",merged)
merged["Score_percentage"] = merged[["Phy","Math","Kannada"]].mean(axis=1)
print("Transformed Datset:\n",merged)