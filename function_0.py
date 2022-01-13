def add(a , b):
    """This function uses only 2 operator and 1 operand at a time... """
    return (a + b)

def sub(a , b):
    return (a - b)

def mul(a , b):
    return (a * b)

def div(a , b):
    return int(a / b)

p = input("Do you want to check the DocString:\n")
if p == 'yes' or p == 'Yes' or p == 'Y' or p == 'y':
    print(add.__doc__)
else:
    print("Okay:")

x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))
s = add(x,y)
t = sub(x,y)
p = mul(x,y)
q = div(x,y)
print("Addition",s)
print("Substraction",t)
print("Multiplication",p)
print("Division",q)


