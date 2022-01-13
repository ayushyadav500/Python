## uses of if elif else...

a = int(input("Enter Your Age\n"))
if 1<= a < 18:
    print("You Are Not ELigible To Drive")
elif a == 18:
    print("You Have To Report To Office First")
elif a == 0:
    print("Wrong Input")
else:
    print("You Can Drive")