import numpy as np

data = np.random.randint(0,100,15)
print("Original Data: \n",data)

threshold = 50

binary_mask = np.where(data>threshold,1,0)
print("Binary Mask: \n",binary_mask)