import numpy as np

arr = np.array([10,20,30,40,50])

normalize = (arr - np.min(arr))/(np.max(arr)-np.min(arr))
print(normalize)