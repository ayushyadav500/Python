lst = ['Ayush','Yadav','Kaalu','Ashu','Rishi','Bhaskar']

# For even values including zero...
a = 0 
for i in lst:
    if a%2 is  0:
        print(i)
    a += 1
print("\n")   

# For odd values...
a = 1
for i in lst:
    if a%2 is 0:
        print(i)
    a += 1
print("\n")

# Using enumerate function...
for index,item in enumerate(lst):
    if index%2 is 0:
        print(item)
    
        