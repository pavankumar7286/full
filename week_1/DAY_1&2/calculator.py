def add(a, b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a*b 
def div(a,b):
    if b==0:
        return " division by zero is not allowed"
    return a/b
def mod(a,b):
    return a%b

a =int(input("Enter A: "))
b =int(input("Enter B: "))

print("\nMENU")
print("\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.MOD\n6.EXIT")
value =int(input("enter your choice : "))
while True:
    match value:
        case 1:
            print(add(a,b)) 
            break
        case 2:
            print(sub(a,b))
            break
        case 3:
            print(mul(a,b))
            break
        case 4:
            print(div(a,b))
            break
        case 5:
            print(mod(a,b))
            break
        case 6:
            exit()
        case _:
            print("invalid choice")
            break


