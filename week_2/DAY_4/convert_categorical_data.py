import pandas as pd

df = pd.DataFrame({
    "Name": ["Pavan","Nithya"],
    "Age": [29,27],
    "hobbies": ["songs","dance"],
    "Place": ["hvr","mys"]
})

# Apply one-hot encoding
df_encoded = pd.get_dummies(df, columns=["Name","hobbies","Place"])

print(df_encoded)
