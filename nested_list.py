# Create a nested list which contains names of students and their marks and print second lowest marks....

record = []
n = int(input('enter number of elements::'))
for i in range(n):
    x = input('enter name::')
    y = int(input('enter number::'))
    record.append([x,y])
#print(record)
print(sorted(record))