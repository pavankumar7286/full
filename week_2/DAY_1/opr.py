import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# print(np.sqrt(arr))
# print(np.max(arr))
# print(np.min(arr))

print(arr[2])
print(arr[::-1])
print(arr[1:5])

reshape=arr.reshape(3,5)
print(reshape)