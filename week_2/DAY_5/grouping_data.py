import pandas as pd
data = {
    # "name":["abi","chin","fig","blo"],
    "class":["A","B","C","A","B","C"],
    "Score":[87,79,97,69,84,76],
    "Age":[18,19,20,17,12,15]
}
df = pd.DataFrame(data)

print("original dataset:\n",df)

grouped = df.groupby("class").mean()
# grouped = df.groupby("name").agg(
#     {
#         "class":"first",
#         "Score":"mean",
#         "Age":"mean"
#     }
# )
print(grouped)

stats =  df.groupby("class").agg(
    {"Score": ["mean","max","min"],"Age":["mean","max","min"]}
)
print(stats)