import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# data = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
data = np.random.rand(5,5)  # Example data for heatmap
# sns.heatmap(data, annot=True, cmap='coolwarm')
df = pd.DataFrame(data)
sns.pairplot(df, diag_kind="auto")  # Pairplot with KDE on the diagonal
plt.title("Heatmap Example")
plt.show()