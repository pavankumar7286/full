import numpy as np

arr = np.random.uniform(1,100,size=(3,3))
print("Random Floats: \n",arr)

normalize = (arr - np.min(arr))/(np.max(arr)-np.min(arr))
print(normalize)