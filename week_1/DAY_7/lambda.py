add = lambda x,y: x+y
print(add(5,8))

subtract = lambda x,y: x-y
print(subtract(10,4))

multiply = lambda x,y: x*y
print(multiply(6,7))

divide = lambda x,y: x/y
print(divide(20,5))

numbers = [1,2,3,4,5]

#map
squares = map(lambda x:x**2,numbers)
print(list(squares))

#filter
even =filter(lambda x:x%2==0,numbers)
print(list(even))

#reduce
from functools import reduce
product = reduce(lambda x,y:x*y,numbers)
print(product)  