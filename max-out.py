# Find largest number in a list without using max function.....
l = []
n = int(input("Enter number of ekements in list\n"))
for i in range(n):
    l.append(int(input()))

s = l[0]

for i in range(1,n):
    if l[i] > s:
        temp = s
        s = l[i]
        
print(s)
'''
maxout = max(l)     # With max funtion.
print(maxout)'''