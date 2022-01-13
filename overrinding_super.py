## CONCEPT OF OVERRIDING AND SUPER....

from typing import ClassVar


class A:
    classvar1 = 'Hello world'
    def __init__(self):
        self.var =  'Bye Bye'
        self.classvar1 = 'Hello Bye'
        self.special = 'Something Special'
    
class B(A):
    classvar2 = 'Bye Bye World'
    def __init__(self):     # 1 #
        super().__init__()
        self.var1 =  'Bye1 Bye1'
        self.classvar1 = 'Hello1 Bye1'
    ''' def __init__(self):         # 2 #
        self.var1 = 'Bey1 Bey1'
        self.classvar1 = 'Hello1 Bye1'
        super().__init__()'''

    
    
a = A()
b = B()
# OVERRIDING #
#print(b.classvar1)  #Here first it will to class B and find classvar1 arguement, if not found in class B then it will move to drived class. 
#print(a.classvar1)
print(b.special,b.classvar1)
'''Here in b.special it will go to class B and find special, when not inside the constructor of class B,
it will get a constructor override (super().__init__()) it will send it to the Inherited/Derived class A,
where it will get special variable inisde the constructor but when we try to print b.classvar1
it will not print the values of class A it will come back and print the values of class B.'''

''' But as we can se in # 2 # supper class is written in the last so first it will check the values of class B,
then it will send to class A and after that it will print the class variable(classvar1) of class A only.'''