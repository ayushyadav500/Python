import time
from functools import lru_cache
lru_cache(maxsize=4)
def myfunc(x):
    time.sleep(2)
    return x

myfunc(1) 
print('hi')
# myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
myfunc(1)
print('bhaskar')
myfunc(2)
myfunc(3)
print('ayush')
myfunc(4)
print('w')
myfunc(5)
