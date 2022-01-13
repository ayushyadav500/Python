# Program to make a faulty calc which will print all the answers correctly except the following :-
#   45 * 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4...


operat = str(input("Enter Operator"))
if operat.isnumeric():
    print("Wrong")
    exit()
    
n1 = input("Enter First Operand:\n")
if n1.isalpha():
    print("Enter valid numer:")
    exit()
else:
    a = int(n1)
    
n2 = input("Enter Second Operand:\n")
if n2.isalpha():
    print("Enter valid numer:")
    exit()
else:
    b = int(n2)

if operat == '*':
    if a == 45 and b == 3 or a == 3 and b == 45:
        print(555)
    else:
        result = a * b
        print(result)

if operat == '+':
    if a == 56 and b == 9 or a == 9 and b == 56:
        print(77)
    else:
        result = a + b
        print(result)

if operat == '/':
    if a == 56 and b == 6:
        print(4)
    else:
        result = a / b
        print(result)
if operat == '-':
    result = a - b
    print(result)
