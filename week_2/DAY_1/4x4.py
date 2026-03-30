import numpy as np


arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)

print("sum of rows: ",sum(arr[0]),sum(arr[1]),sum(arr[2]),sum(arr[3]))
print("sum of columns: ",sum(arr[:,0]),sum(arr[:,1]),sum(arr[:,2]),sum(arr[:,3]))