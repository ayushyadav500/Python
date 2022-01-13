# Use of while...

#i = 1
"""while(i<100):
    i = i + 1
    print(i)

print("Congrats")

while(True):
    if i < 5:
         i = i + 1
         continue
    if i == 8:
        print("bye")
        break
    if i < 10:
        i = i + 1
        print(i)
    
print("out")
    
"""

while(True):
    i = int(input("Enter a number:\n"))
    if i > 100:
        print("Congrats:")
        break
    else:
        print("Try Again:")
        continue