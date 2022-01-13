
try:
    f1 = open('bastard.txt')

except Exception as e:
    print(e)
    
finally:  # it will execute whether try or except run or not.
    print('bye')

print('hello')