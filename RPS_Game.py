import random
c = 0
u = 0
while True :
    computer = random.choice(['rock', 'paper', 'scissor'])
    user = input("What you will choose:(rock,paper,scissor)\n")
    list = ['rock','paper','scissor']
   
    if user not in list:
        print("wrong ")
    if user == computer:
        print('Tie')
        
    elif user == 'rock':
        if computer == 'paper':
            c = c + 1
            print('lose')
        else:
            u = u + 1
            print('win')
    elif user == 'paper':
        if computer == 'scissor':
            c = c + 1
            print('lose')
        else:
            u = u + 1
            print('win')
    elif user == 'scissor':
        if computer == 'rock':
            c = c + 1
            print('lose')
        else:
            u = u + 1
            print('win')
    inp = input("\nplay again ?\n")
    if inp == 'y' or inp == 'Y' or inp == 'yes' or inp == 'Yes' or inp == 'YES' :
        continue
    else:
        print('Scores are::')
        print(f'Player got {u} scores')
        print(f'Computer got {c} scores\n')
        print("--THANKS FOR PLAYING--")
        break