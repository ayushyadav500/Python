class Abc:
    counter = 0 
    @staticmethod
    def  show_counter():
        print(Abc.counter)
        print(Abc().a)
    def __init__(self):
        self.a = 1
    def disp(self):
        print(self.a)
        print(Abc.counter)
obj = Abc()
obj1 = Abc()
obj.show_counter()
obj1.show_counter()
obj.disp()
obj1.disp()
        