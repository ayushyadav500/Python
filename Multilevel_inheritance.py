## Multi-level inheritance...  Private, Public, Protected...
class DAD:
    base = 1            # Public.
    _front = 5          # Protected.
    __bag = 2          # Private.
    
class SON(DAD):     # It inherits DAD class.
    dance = 3        
    _dancer = 2      
    __prdance = 5    
    def isdance(self):
        print(f'Yes I know {self.dance} types of dance')
        
class GRANDSON(SON):         # It inherits SON class.
    dance = 10
    _prodancer = 33
    __pridancer = 65
    #print(base)
    def todance(self):
        return f'I am a big fan of Michael Jackson,I know {self.dance} types of dance'
    
    
        
a = DAD()
b = SON()
c = GRANDSON()
'''print(c.todance())
print(c.dance)
print(c.base)       # It can access all the attributes, methods, constructors of all the three classes as it inherits all three.
print(DAD.base)
print(GRANDSON.base)
print(SON.base)
print(a.base)
print(c.base)
print(b.base)
print(SON._front)   # Accessing one protected attribute from another class.
print(GRANDSON._front)
print(b._front)
print(c._front)'''

print(a._DAD__bag)
print(b._DAD__bag)
print(c._DAD__bag)

#print(a._SON__prdancer)  # You can't access it from .