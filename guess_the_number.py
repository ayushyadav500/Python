import random
n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,28,29,30]
print("There are 30 numbers in this game(1-30) you have to guess the right number:")
print("You only have 5 chances: Good Luck!")
a = 1
while a == 1:
    b = 0
    while(b<5):
        c = random.choice(n)
        inp = int(input("Enter Your Choice:\n"))
        if b == 4:
            print("Sorry! Game Over:")
            break
        elif c == inp:
            print("Bingo you got it:")
            print("You got in ",b,'chances')
            break
        else:
            print("Try Again:")
            b = b + 1
            print(5-b,' Chances left:')
            continue
    a = 0
    if a == 0:
        break