import matplotlib.pyplot as plt

#line plot
years =[
    2008, 2009, 2010, 2011, 2012, 2013, 
    2014, 2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024, 2025
]
runs = [
    165, 246, 307, 557, 364, 634, 
    359, 505, 973, 308, 530, 464, 
    466, 405, 341, 639, 741, 731
]
plt.figure(figsize=(12,6))
plt.bar(years,runs,color="goldenrod")
plt.title("Virat kohli's runs over the years in IPL")
plt.xlabel("years")     
plt.ylabel("runs")
plt.xticks(years, rotation=0)
plt.legend(["Runs"], loc="upper left")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()