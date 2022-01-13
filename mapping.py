## MAPPING FUNCTION.....
from functools import reduce  # Import reduce from functools module..

# Using in-built function..
l = ['1','2','6','7']
l = list(map(int,l))
print(l)
for i in l:
    print(i,end=' ')


# Using our own function...    
def sq(a):
    return a*a

num = [10,2,3,4,2,1,3,4]    
square = list(map(sq,num))
for i in square:
    print(i,end=' ')
    
def add(a):
    return a+a

s = [2,3,1,4,2,2]
addition = list(map(add,s))
print(addition)

# Passing fn to values..
def sq(a):
    return a*a
def cube(a):
    return a*a*a
# Store function in list..
fn = [sq,cube]
for i in range(6):
    value = list(map(lambda x:x(i),fn))
    print(value)
    
# Reduce
    
l = [1,2,3,4]
s = reduce(lambda a,b:a+b,l) # reduces list to their addition...
print(s)

# Using set
def greator(num):
    return num > 5

s = (6,1,2,3,7,384,5)
s = set(filter(greator,s))
print("Filter",s,'\n')

l = reduce(lambda x,y:x+y,s)
print("Reduce",l)