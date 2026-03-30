import numpy as np

arr = np.random.rand(3,4,5)
print("Random 3D Array: \n",arr)

mean_axis0 = np.mean(arr, axis=0)
print("Mean along axis 0: \n",mean_axis0)

mean_axis1 = np.mean(arr, axis=1)
print("Mean along axis 1: \n",mean_axis1)

mean_axis2 = np.mean(arr, axis=2)
print("Mean along axis 2: \n",mean_axis2)