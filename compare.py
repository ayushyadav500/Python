s = ["+,-,/,*"]
t = ["int,float,double,char"]
p = ["if,else,elif"]
w = ["@,#,$,&,!"]

a = ['identifiers']
b = ['keywords']
c = ['operators']
d = ['Special Symbol']
e = ['wrong']

lst = []
inp = input()
x = inp.split
for i in range(len(x)):
    if x[i] in s:
        lst.append(c)
    
    if x[i] in t:
        lst.append(a)

    if x[i] in p:
        lst.append(b)

    if x[i] in w:
        lst.append(d)

    

print(lst)