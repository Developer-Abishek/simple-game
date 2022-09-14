
import random
def GameWin(comp,plyr):
    if comp==plyr:
        return print("Game is draw")

    if comp=="r":
        if plyr=="p":
            return True
        elif plyr=="s":
            return False

    if comp=="p":
        if plyr=="s":
            return True
        if plyr=="r":
            return False

    if comp=="s":
        if plyr=="p":
            return False
        if plyr=="r":
            return True    


a = random.randint(1,3)
if a==1:
    comp="r"
elif a==2:
    comp="p"
else:
    comp="s"

plyr=input("enter your choice rock(r),paper(p),scissor(s) : ")
plyr = plyr.lower() 
check = GameWin(comp,plyr) 
print (f" choice of computer was {comp}")
print (f"Your choice was {plyr}")
if check:
    print("Great you win!")
else:
    print("Better luck next time!")     
