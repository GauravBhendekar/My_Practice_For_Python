# snake Water Gun Game
import random
while True:
    play="y"
    if play=="y":
        Choice=int(input("""0.Snake \n1.Water\n2.Gun"""))
        comchoice=random.randint(0,2)
        print(f"computer choose { "snake" if comchoice==0 else "Water" if comchoice==1 else "Gun"  } And you -->",end=" ")
        lst=[["Draw","Loos","Win"],["Win","Draw","Loos"],["Loos","Win","Draw"]]
        print(lst[comchoice][Choice])
        play=input("enter whether you want to play(y) or not(n)")
    else:
        break
    