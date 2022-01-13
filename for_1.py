# Use of for...

list1 = ["hello",6,60,'the',1212121,1,0,1,2,3,4,5,10,'bye']
print(list1)
for i in list1:
    if str(i).isnumeric() and i < 6:
        print(i)

