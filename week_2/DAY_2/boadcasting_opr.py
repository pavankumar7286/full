import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([1,0,-1])

res = matrix +vector
print("ADD: ",res)

res = matrix -vector
print("SUB: ",res)

res = matrix *vector
print("MUL: ",res)

res = matrix /vector
print("DIV: ",res)
