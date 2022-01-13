
print("You have 10 lifes in this game\n","You entered in the snake water gun game\n")
import random
list = ["snake","water","gun"]
while(1):

        d=0
        e=0
        b=1
        while(b<12,d<b,e<b):
            b=b+1
            if b==12:
                print("no. of life is completed")
                break
            c = random.choice(list)
            a = input("your turn ,enter s for snake\w for water\g for gun:\n")
            if c=="snake":
                if a=="s":
                    print("no one win",end="    "),         print("no. of lifes remained:",11-b)
                elif a=="w":
                    d=d+1
                    print("computer is winner",end="   "),      print("no. of lifes remained:",11-b,end="      "),     print("no. of points computer gained",d)

                elif a=="g":
                    e=e+1
                    print("you are winner",end="      "),     print("no. of lifes remained:",11-b,end="       "),    print("no. of points you gained",e)

                    continue
            elif c == "water":
                if a == "w":
                    print("no one win", end="    "), print("no. of lifes remained:", 11-b)
                elif a == "g":
                    d=d+1
                    print("computer is winner", end="   "), print("no. of lifes remained:",11-b,end="    "),print("no. of points computer gained",d)

                elif a == "s":
                    e=e+1
                    print("you are winner", end="      "), print("no. of lifes remained:",11-b,end="     "),print("no. of points gained by you",e)

                    continue
            elif c == "gun":
                if a == "g":
                    print("no one win", end="    "), print("no. of lifes remained:",11-b)
                elif a == "s":
                    d=d+1
                    print("computer is winner", end="   "), print("no. of lifes remained:",11-b,end="     "), print("no. of points computer gained",d)

                elif a == "w":
                    e=e+1
                    print("you are winner", end="      "), print("no. of lifes remained:",11-b,end="     "), print("no. of points you gained",e)

                    continue
        if d>e:
                print("computer is winner","\ntotal no. of points computer gained:",d,end="   "), print("\nyou are losser","\ntotal no. of points you gained:",e)
        elif d<e:
                print("you are winner","\ntotal no. of points you gained:",e,end="    "), print("\ncomputer is loser","\ntotal no. of points computer gained:",d)
        else:
                print("pls restart the game,no one is winner")
        k = input("enter Y for restart the game or N for quite the game:")
        if k=="Y":
            print("you restart the snake water gun game")
            continue
        elif k=="N":
            print("you quite the snake water gun game")
            break