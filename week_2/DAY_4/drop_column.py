import numpy as np
import pandas as pd

data= {
    "A":[1,np.nan,np.nan,np.nan,np.nan],
    "B":[5,np.nan,7,8,9],
    "C":[np.nan,np.nan,np.nan,np.nan,np.nan]
}
df=pd.DataFrame(data)
print(df)
threshold = 0.5
df_cleaned = df.dropna(thresh=int((1-threshold)*len(df)),axis=1)
print(df_cleaned)
