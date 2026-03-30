import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

# print(arr[0][0])
# print(arr[1][2])
# print(arr[2][1])
# print(arr[0])
# print(arr[:,0])
# print(arr[0,:])
# print(arr[1:3,1:3])

transpose_arr = arr.T
print(transpose_arr)

another_arr = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("Addition:\n",arr+another_arr)

print("Subtraction:\n",arr-another_arr)
