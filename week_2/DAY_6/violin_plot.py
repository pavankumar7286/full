import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example datasets
data = {
    "Virat Kohli": [165, 246, 307, 557, 364, 634, 359, 505, 973, 308, 530, 464, 466, 405, 341, 639, 741, 731],
    "MS Dhoni":    [150, 220, 310, 480, 370, 600, 390, 450, 890, 320, 510, 470, 490, 420, 360, 610, 700, 720],
    "AB de Villiers":    [180, 260, 330, 540, 380, 620, 350, 490, 960, 300, 520, 460, 480, 410, 350, 630, 710, 740]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Melt into long format for seaborn
df_melted = df.melt(var_name="Player", value_name="Runs")

# Box plot
plt.figure(figsize=(10,6))
sns.boxplot(x="Player", y="Runs", data=df_melted, palette="Set2")
plt.title("Box Plot of IPL Runs Distribution")
plt.show()

# Violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Player", y="Runs", data=df_melted, palette="Set2")
plt.title("Violin Plot of IPL Runs Distribution")
plt.show()
