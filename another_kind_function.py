## Program to illustrate the use of *args  *kwargs...

def school(normal,*a,**b):  # (normal value,*args,**kwargs)...
    print(normal,'\n')      
    print('List:')
    for i in a: # list...
        print(i)
    print("\nDictionary:")
    for key,value in b.items(): ## Dictionary...
        print(f"{key} is a {value}")  ## Using f-string to print dictionary... 
    
    
inp = input("Enter anything\n")   
s = ['Ayush','Kaalu','Shukla','Ajay']
dic = {'Ayuh' : 'Good Boy',
       'Ajay' : 'Bad Boy',
       'kaalu' : 'Best Friend',
       'Ashu' : 'No one',
       'Aakash' : 'Nashedi'}
school(inp,*s,**dic) # passing all the three values to the function...
