import pandas as pd
import numpy as np

data ={
    "name":['pavan','dhanu','nithya','vinnu'],
    "physics":[78,90,61,99],
    "chemistry":[88,78,22,82],
    "mathematics":[64,74,85,97],
    "biology":[87,43,56,92]
}
df = pd.DataFrame(data)
 
df["Average"]= df[["physics","chemistry","mathematics","biology"]].mean(axis=1)
df["Result"] = df[["physics", "mathematics","chemistry", "biology"]].apply(lambda row: "Fail" if any(row < 40) else "Pass", axis=1)
print(df)