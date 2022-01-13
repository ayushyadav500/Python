# Using range() function.
list = []
num = int(input("Enter the number of elements in list"))
for i in range(num):
    list.append(int(input("Enter the list")))
total = sum(list)
print("the total is $",total,sep='')