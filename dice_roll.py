import random
a = 1

while a == 1:
    def roll_dice():
        dice = random.randint(1,6) + random.randint(1,6)
        return dice
        
    player1 = input("Enter Player1 Name\n")
    player2 = input("Enter Player2 Name\n")
    roll1 = roll_dice()
    roll2 = roll_dice()
    print(player1 ,"rolled",roll1)
    print(player2 ,"rolled", roll2)
    if roll1 == roll2:
        print("TIE")
    elif roll1 > roll2:
        print(player1,"WIN:")
    else:
        print(player2,"WIN:")
    
    print("Press y to play again:\nIf not press n to quit:")
    s = input("Play Again ?\n")
    if s == 'y':
        continue
    elif s == 'n':
        break
    else:
        print("Wrong Input:")
        print("Sorry! Game Over:")
    
       