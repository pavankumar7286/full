import numpy as np

dataset = np.random.randint(0,100,size=(5,5))
print("Random Dataset: \n",dataset)

dataset[dataset>25]=0
print("Modified Dataset: \n",dataset)


print("mean: ",np.mean(dataset))
print("sum: ",np.sum(dataset))
print("std: ",np.std(dataset))