# snake Water Gun Game
'''Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water.
Gun vs. Snake: Gun will kill the snake and win.'''
import random
while True:
    play="y"
    if play=="y":
        Choice=int(input("""0.Snake \n1.Water\n2.Gun"""))
        comchoice=random.randint(0,2)
        print(f"computer choose { "snake" if comchoice==0 else "Water" if comchoice==1 else "Gun"  } And you choose{"Snake" if Choice==0 else "Water" if Choice==1 else "Gun" if Choice==2 else "you do cheate" } hence you -->",end=" ")
        lst=[["Draw","Loose","Win"],["Win","Draw","Loose"],["Loose","Win","Draw"]]
        print(lst[comchoice][Choice])
        play=input("enter whether you want to play(y) or not(n)")
    else:
        break
    