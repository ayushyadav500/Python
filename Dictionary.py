##Using Dictionary.
#a = {'Ayush':'Good Boy',
#     'Aman': 'Bad boy', 
#     'ashu':'my friend'}
#print(a['Ayush'])   # Prints the definition of ayush
#b = a.get('Ayush')+ a.get('Aman')   # conacatenates two definitions
#print(b)

# Combination of a list and dictionary 
#breakfast = ['Egg','milk','coffee']
#lunch = ['snacks','tea/coffee + biscuits','dosa']
#dinner = ['meal','rice','half meal']
menu = (['Egg',['milk','coffee']],['snacks','tea/coffee + biscuits','dosa'],['meal','rice','half meal'])
#print(breakfast)
#print(dinner)
#print(lunch)
#print(menu)
print(menu[0][1])
#print(menu[1][0])

# Menus = {'breakfast' : ['Egg','milk','coffee'],
#         'lunch' : ['snacks','tea/coffee + biscuits','dosa'],
#         'dinner' : ['meal','rice','half meal']}
# print(menu)

# contact details of students.

# contact = { 
#     'number' :5,
#          "student":
#                 [
#                   {'Ayush' : 'email =ayush09yadav@gmail.com'},
#                   {'yadav' :  'email = ayushyadav0906@gmail.com'},
#                   {'Dev'   :  'email = Dev1234@gmail.com'},
#                   {'bastard': 'email = noone000@gmmail.com'},
#                   {'kaalu': 'email = pagalpanti@gmail.com'}
#                 ]
#}  
# print(contact['student'])
#for student in contact['student']:
#    print("\n",student['name'])
'''contact = {
    "Ayush":['Branch':'cs',
            'class':'3rd',
            'surname':'yadav']
    "bha":['branch':'en',
          'class':'3rd',
          'surnname':'g']
}
    '''