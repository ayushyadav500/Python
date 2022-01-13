# Class EMPLOYEE with all the neccessary details....
from datetime import date

class EMPLOYEE:
    
    def display(self):
        return f'Employee id is {self.id}.\nName is {self.name}.\nAge is {self.age}.\nDesignation is {self.designation}.\nAddress {self.address}.\nDepartment {self.department}.\nDate of Birth {self.dob}'
     
    def __init__(self,EMPID,Name,Age,Designation,Address,Department,DOB):
        self.id = EMPID
        self.name = Name
        self.age = Age
        self.designation = Designation
        self.address = Address
        self.department = Department
        self.dob = DOB
        
    @classmethod
    def str(cls,string):
        s =  string.split('-')
        print(s)
        return cls(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
      
        
Ayush = EMPLOYEE(512,'Ayush',20,'Manager','B-788 Andha Kuwa Road Kanpur','CS',date(2000,6,9))
kaalu = EMPLOYEE.str('222-Bhaskar-22-HOD-Panki-CS-date(2000,8,4)')
print('\n')
print(kaalu.display())
