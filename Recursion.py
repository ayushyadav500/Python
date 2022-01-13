## Recursion in factorial and fibonacci...


## Iterative method of factorial.
def fact(n):
    f = 1
    for i in range(n):
        f=f * (i+1)
    return f
    

# Recursive method.
def refact(n):
    if n == 1:
        return 1
    else:
        return n * refact(n-1)
    
num = int(input("Enter Number:\n"))
print("Recursive Factorial is:\n",fact(num))
print("Iterative Factorial is:\n",refact(num))


# Fibonacci series.
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Enter Number:\n"))
print(fibo(num))