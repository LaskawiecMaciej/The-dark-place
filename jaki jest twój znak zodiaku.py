import time
import datetime


def strzałka(kierunek):
    #FUNKCJA EKSTREMALNIE PROFESJONALNA
    if(kierunek=="DÓŁ"):
        for i in range(3):
            print("    @ @ @ @ @     ")
            pozycja=0
            index=0
        print("@ @ @ @ @ @ @ @ @  \n  @ @ @ @ @ @ @  \n    @ @ @ @ @ \n      @ @ @  \n       @ @ \n        @" )
    else:
        print("strzałka działa tylko w dół... sorry")


print( "############    PROGRAM KTÓRY SPRAWDZA JAKI MASZ ZNAK ZODIAKU    ############## \n")


x=1
while(x<2):
    data=str(input("Podaj swoją datę urodzenia dd/mm/rrrr :  "))
    try:
        day=int(data[0]+data[1])
        month=int(data[3]+ data[4])
        year=int (data[6]+ data[7] + data[8] +data[9])
    except ValueError:
        print("\n")
        time.sleep(1)
        print("hmmm...")
        time.sleep(0.5)
        print("hmmmmm...")
        time.sleep(0.5)
        print("WPISAŁEŚ JAKIEŚ GŁUPOTY.. ALBO PODAŁEŚ DATĘ W NIEPRAWIDŁOWYM FORMACIE: \nPAMIĘTAJ PODAJ ZERA ORAZ ODDZIEL ELEMENTY DATY -\nSPRÓBUJ JESZCZE RAZ")
        continue
    if(day>31):
        print("WPROWADZIŁEŚ BŁĘDNĄ DATĘ - DZIEŃ")
    if(year<1990 or year>2025):
        print("\n")
        time.sleep(1)
        print(".................")
        time.sleep(1)
        print("\n")
        time.sleep(1)
        print(".................")
        time.sleep(1)
        print("\n")
        time.sleep(1)
        print(".................")
        time.sleep(1)
        print("\n")
        time.sleep(1)
        print("Co to wogóle za rok ...? ten człowiek jeszcze się nawet nie urodził ")
        continue


    print("\n")
    strzałka("DÓŁ")
    print("\n")
    if(month == 1):
        if(day<20):
            print("TWÓJ ZNAK ZODIAKU TO KOZIOROŻEC")
        elif(day>=20):
            print("TWÓJ ZNAK ZODIAKU TO WODNIK")

    if(month == 2):
        if(day<19):
            print("TWÓJ ZNAK ZODIAKU TO WODNIK")
        elif(day>=19):
            print("TWÓJ ZNAK ZODIAKU TO RYBY")
    if(month == 3): 
        if(day<21):
            print("TWÓJ ZNAK ZODIAKU TO RYBY")
        elif(day>=21):
            print("TWÓJ ZNAK ZODIAKU TO BARAN")
    if(month == 4):
        if(day<19):
            print("TWÓJ ZNAK ZODIAKU TO BARAN")
        elif(day>=19):
            print("TWÓJ ZNAK ZODIAKU TO BYK")
    if(month == 5):
        if(day<21):
            print("TWÓJ ZNAK ZODIAKU TO BYK")
        elif(day>=21):
            print("TWÓJ ZNAK ZODIAKU TO BLIZNIETA")
    if(month == 6):
        if(day<21):
            print("TWÓJ ZNAK ZODIAKU TO BLIZNIETA")
        elif(day>=21):
            print("TWÓJ ZNAK ZODIAKU TO RAK") 
    if(month == 7): 
        if(day<23):
            print("TWÓJ ZNAK ZODIAKU TO RAK")
        elif(day>=23):
            print("TWÓJ ZNAK ZODIAKU TO LEW") 
    if(month == 8):
        if(day<23):
            print("TWÓJ ZNAK ZODIAKU TO LEW")
        elif(day>=23):
            print("TWÓJ ZNAK ZODIAKU TO PANNA ") 
    if(month == 9):
        if(day<22):
            print("TWÓJ ZNAK ZODIAKU TO PANNA")
        elif(day>=23):
            print("TWÓJ ZNAK ZODIAKU TO WAGA") 
    if(month == 10):
        if(day<22):
            print("TWÓJ ZNAK ZODIAKU TO WAGA")
        elif(day>=23):
            print("TWÓJ ZNAK ZODIAKU TO SKORPION") 
    if(month == 11): 
        if(day<22):
            print("TWÓJ ZNAK ZODIAKU TO SKORPION")
        elif(day>=23):
            print("TWÓJ ZNAK ZODIAKU TO STRZELEC") 
    if(month == 12):
        if(day<22):
            print("TWÓJ ZNAK ZODIAKU TO STRZELEC")
        elif(day>=22):
            print("TWÓJ ZNAK ZODIAKU TO KOZIOROŻEC") 
    elif(month<1 or month > 12):
        print("PODAŁEŚ JAKIŚ NIE ISTNIEJĄCY MIESIĄC...")

    print("\n")
    decyzja=input("CZY CHCESZ SPRAWDZIĆ KOLEJNĄ DATĘ?  Y / N  : ")
    print("\n")
    if(decyzja == "n" or decyzja == "N"):
        break
        print("ALE NUDA TEN PROGRAM.. NIE DOŚĆ ŻE BRZYDKI TO I MAŁO PRAKTYCZNY... PÓŁ GODZINY PISANIA A KTOŚ POBAWI SIĘ PIĘĆ MINUT....")
        time.sleep(1)
        time.sleep(1)