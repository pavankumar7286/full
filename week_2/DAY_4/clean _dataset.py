import pandas as pd
import numpy as np

data = {
    "Name":["pavan","nithya","pooja","david"],
    "Age":[25,np.nan,30,23],
    "Score":[58,60,np.nan,90]

}

df =pd.DataFrame(data)
print("original data:\n",df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

print("Dataset :\n",df)

df = df.rename(columns={"Name":"Student Name","Score":"Exam Score"})
print("renamed dataset :\n",df)