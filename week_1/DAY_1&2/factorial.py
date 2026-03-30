num = int(input("Enter a number to fin its Factorial:"))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
print(f"The factorial of {num} is {factorial(num)}")
    
