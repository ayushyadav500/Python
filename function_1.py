def ASMD(a , b):
    """This function uses only 2 operator and 1 operand at a time and gives all the calculated values... """
    return ([a + b],[a-b],[a*b],[a/b])

p = input("Do you want to check the DocString:\n")
if p == 'yes' or p == 'Yes' or p == 'Y' or p == 'y':
    print(ASMD.__doc__)
else:
    print("Okay:")
    
x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))
s = ASMD([x,y])
print("Answers are:\n",s)
