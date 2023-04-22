from enum import IntEnum
import random



print("Welcome in the scisor/paper/rock game")
print("Rules are very easy and everybody knows them... \n ...rock beat scisors, scisors peats paper, paper beats rock")
while (2<3) :
    print("You need to make your choice!")
    PlayerChoice=(input("S/R/P  scissors/rock/paper:  "))
    ChoiceList=["S","s","scissors","R","r","rock","P","p","paper"]



    if (PlayerChoice==ChoiceList[0] or PlayerChoice==ChoiceList[1] or PlayerChoice==ChoiceList[2]):
        PlayerHas = 1
    elif(PlayerChoice==ChoiceList[3] or PlayerChoice==ChoiceList[4] or PlayerChoice==ChoiceList[5]):
        PlayerHas=2
    elif(PlayerChoice==ChoiceList[6] or PlayerChoice==ChoiceList[7] or PlayerChoice==ChoiceList[8]):
        PlayerHas=3
    else:
        print(" \n You have choosen something wrong... try again")
        continue

    NPCchoice=(random.randint(1,3))

    if(PlayerHas==1 and NPCchoice == 2):
        print("I have choosen rock! haha you lost")
    elif(PlayerHas==1 and NPCchoice == 3):
        print("I have choosen paper! congratulation you won!")
    elif(PlayerHas==1 and NPCchoice == 1):
        print("I have choosen the same.. there is no winner")

    elif(PlayerHas==2 and NPCchoice == 2):
        print("I have choosen the same.. there is no winner")
    elif(PlayerHas==2 and NPCchoice == 3):
        print("I have choosen rock! haha you lost")
    elif(PlayerHas==2 and NPCchoice == 3):
        print("I have choosen paper! congratulation you won!")

    elif(PlayerHas==3 and NPCchoice == 2):
        print("I have choosen rock! congratulation you won!")
    elif(PlayerHas==3 and NPCchoice == 3):
        print("I have choosen the same.. there is no winner")
    elif(PlayerHas==3 and NPCchoice == 1):
        print("I have choosen scissors! you lost you pussy!")
    else:
        print(" \n you morron the game is over becouse you are stupid")
    print(" \n Lets play again....")