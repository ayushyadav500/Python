'''a = 'This is {} {}'
m = 'Ayush'
n = 'Yadav'

b1 = a.format(m,n)
print(b1)

b2 = a.format('Rishi','Yadav')
print(b2)

s = 'This is {1} {0}'
b3 = s.format(m,n)
print(b3)

d = f'This is {m} {n} {1*100}'
print(d)
'''
print("Enter")
string = input()
word = string.split(' ')
rev = list(reversed(word))
connector = " "
r = connector.join(rev)
s = r.swapcase()
print(s)
