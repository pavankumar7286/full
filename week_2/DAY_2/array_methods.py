import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print("Sum :",np.sum(arr))
print("Mean :",np.mean(arr))
print("Median :",np.median(arr)) 
print("Standard Deviation :",np.std(arr))
print("Variance :",np.var(arr))
print("Minimum :",np.min(arr))
print("Maximum :",np.max(arr))

print("Sum of rows: ",np.sum(arr,axis=1))
print("Sum of columns: ",np.sum(arr,axis=0))