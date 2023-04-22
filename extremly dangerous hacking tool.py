import pyautogui as pag
import random
import time
def processDots(process, dotsNumber, addDotTime):
    import time
    print(process ,end="\r")

    for i in range(dotsNumber):
        time.sleep(addDotTime)
        print(".\r",end="\r")

lista=["1","2","3","4","5","6","7","8","9","0","p","o","i","j","u","k","l","g","b","f","s","x","z","e","r","t","y"," ","@","$","%","&","*","<",">","?"]

processDots("BREAKING ACCES", 5 ,0.1)
x=""
for i in range(440):
    x+=random.choice(lista)

print(x)


for i in range(0,1000):
    x=random.randint(100,1400)
    y=random.randint(100,1400)
    pag.moveTo(x,y,0,5)
    time.sleep(0.01)
    x=random.randint(0,1)
    if(x==0):
        print( "ACCES BROKEN STEALLING DATA......")
    else:   
        print( "ACCES BROKEN DELETING DATA......")
   
    
