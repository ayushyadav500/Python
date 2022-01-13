## program to demonstrate lambda(different way to create function in one line) function....


def add(a,b):
# Normal function.....
    return a+b
s=add(5,6)
print(s)

# Without using function just in one line
add = lambda x,y:x+y
a = int(input("Enter First:"))
b = int(input("Enter Second:"))
a = add(a,b)
print(a)


# Nested list sorting....
def sort(n):
    return n[1]

n = [[3,23],[5,3],[2,13],[5,6],[6,0]]
n.sort(key=sort)
print(n)
