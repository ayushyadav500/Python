def add(a , b):
    return (a + b)

def sub(a , b):
    return (a - b)

def mul(a , b):
    return (a * b)

def div(a , b):
    return int(a / b)

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
