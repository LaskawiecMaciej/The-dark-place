
def sumowanie_czasu(skrypt):
    start=time.perf_counter()

    skrypt()

    koniec=time.perf_counter()
    return(koniec-start)


'''TO TYLKO ROZCZAROWUJĄCA FUNKCA STRZAŁKI'''
def strzałka(kierunek):
    if(kierunek=="DÓŁ"):
        for i in range(5):
            print("    @ @ @ @ @     ")
            pozycja=0
            index=0
        print("@ @ @ @ @ @ @ @ @  \n  @ @ @ @ @ @ @  \n    @ @ @ @ @ \n      @ @ @  \n       @ @ \n        @" )
    else:
        print("strzałka działa tylko w dół... sorry")







print("\n \n \n #####################      KALKULATOR GEOMETRYCZNY     #####################")
import math
import time
from enum import IntEnum
def kalkulator_geometryczny():
    while(1<2):
        

        
        print("\n Będziemy pracować na bryłach czy na figurach? B/F:")
       

        BryFig=input()

        if(BryFig== "F")or(BryFig=="f"):

            Wybór_Figury = IntEnum("\n WybórFigury", "koło trójkąt trapez prostokąt")

             
            print("Jaka figura płaska cię interesuje?")


            Fig=int(input("""koło: 1
    trójkąt: 2
    trapez: 3
    prostokąt: 4
    """))

            if(Fig==Wybór_Figury.koło)or(Fig=="k"):
                print("WPROWADŹ NIEZBĘDNE DANE")
                R=int(input("Podaj średnice koła w mm: "))

                print("Podana średnica koła: ", R)
                r2=(R**2)
                
                r3 = (math.pi * r2)
                PoleKoła = (r3)
                
                strzałka("DÓŁ")
                print("Pole koła o podanej śrenicy:", R ,"wynosi:", PoleKoła, "mm")
                ObwódKoła = ( 2 * math.pi * R)
                
                print("Obwód koła o podanej śrenicy:", R ,"wynosi:", ObwódKoła, "mm")

            elif(Fig==Wybór_Figury.trójkąt)or(Fig=="tt"):
                 print("WPROWADŹ NIEZBĘDNE DANE")
                 
                
                 A=int(input("Podaj podstawę trójkąta w mm: "))
                 H=int(input("Podaj wysokość trójkąta w mm: "))
                 print("Podana podstawa trójkąta to: ", A , "a wysokość to: ", H,"mm")
                 PolTr=( A * H / 2)
                 strzałka("DÓŁ")
                 print("Pole tego trójkąta to: ",PolTr, "mm")
            elif(Fig==Wybór_Figury.trapez):
                 
                 
                 print("WPROWADŹ NIEZBĘDNE DANE")
                 A=int(input("Podaj podstawę trapezu w mm: "))
                 B=int(input("Podaj drugą podstawę trapezu w mm: "))
                 H=int(input("Podaj wysokość trapezu w mm: "))
                 print("Podana podstawa trapezu to: ", A , "a wysokość to: ", H,"mm")
                 PolTrap=( (A+B) * H / 2)
                 strzałka("DÓŁ")
                 print("Pole tego trójkąta to: ",PolTrap, "mm")
            elif(Fig==Wybór_Figury.prostokąt)or(Fig=="p"):
                 print("WPROWADŹ NIEZBĘDNE DANE")
                 A=int(input("Podaj podstawę prostokąta w mm: "))
                 B=int(input("Podaj drugą podstawę prostokąta w mm: "))
                 print("Podane podstawy to: ", A , "i", B,"mm")
                 PolPr=( A * B)
                 strzałka("DÓŁ")
                 print("Pole tego prostokąta to: ",PolPr, "mm")
                 ObwPr=(2*A +2*B)
                 print("Obwód tego prostokąta to: ",ObwPr, "mm")
                 print("Wszystkie kąty wynoszą 90 stopni")
                 if(A==B):
                     print("Ten prostokąt jest też kwadratem")
            else:
                 print("\n")
                 print("\n")
                 print("Wpisałeś coś nie tak.. zaczniemy od początku")
                        
        elif(BryFig == "B")or(BryFig=="b"):   
             print("Jaka bryła cię interesuje?")
             
             Wybór_Bryły = IntEnum("Wybór_Bryły", " Kula, Walec, Stożek ,Graniastosłup, Prostopadłościan")

             Bry=int(input("""Kula: 1
Walec: 2
Stożek: 3
Graniastosłup: 4
Prostopadłościan: 5 - """)) 
             if(Bry== Wybór_Bryły.Kula )or(Bry=="k"):
                 print("WPROWADŹ NIEZBĘDNE DANE")
                 R=int(input("Podaj promień kuli w mm: "))

                 print("Podany promień kuli: ", R)
                 r1=(R**2)
                 r2=(4*r1)
                 r3=(math.pi * r2)
                 wynik =(r3)
                 PoleKuli = (wynik)
                 print("Pole całkowite kuli o podanym promieniu:", R ,"wynosi:", PoleKuli, "mm")
                 o1=(R**3)
                 o2=(math.pi*o1)
                 o3=(4/3)
                 o4=(o3*o2)
                    
                 ObjKuli = (o4)
                 strzałka("DÓŁ")
                 print("Objętość kuli o podanym promieniu:", R ,"wynosi:", ObjKuli, "mm")

             elif(Bry==Wybór_Bryły.Walec)or(Bry=="w"):
                 print("WPROWADŹ NIEZBĘDNE DANE")
                 A=int(input("Podaj średnicę podstawy walca w mm: "))
                 R=(A/2)
                 H=int(input("Podaj wysokość walca w mm: "))
                 print("Podana średnica walca to: ", A ,"a więc promień podstawy to:",R, "a wysokość to: ", H,"mm")
                 p1=(R+H)
                 p2=(math.pi*R)
                 p3=(p1*p2)
                 p4=(2*p3)


                 PolWal=(p4)
                 strzałka("DÓŁ")
                 print("Pole tego walca to: ",PolWal, "mm")
                 g1=(R**2)
                 g2=(math.pi*g1)
                 g5=(g2*H)
                 ObjWal=(g5)
                 
                 print("Objętość tego walca to: ",ObjWal, "mm")

             elif(Bry==Wybór_Bryły.Stożek)or(Bry=="s"):
                 print("WPROWADŹ NIEZBĘDNE DANE")
                 A=int(input("Podaj średnicę podstawy stożka w mm: "))
                 R=(A/2)
                 H=int(input("Podaj wysokość stożka w mm: "))
                 print("Podana średnica podstawy stożka to: ", A ,"a więc promień podstawy to:",R, "a wysokość to: ", H,"mm")
                 p1=(R**2)
                 p2=(math.pi*p1)

                 PolSto=(p2)

                 o1=(R**2)
                 o2=(math.pi*o1)
                 o3=(o2*H)
                 o4=(1/3*o3)
                 o5=(o4)

                 ObjSto=(o5)
                 strzałka("DÓŁ")
                 print("Pole tego stożka to: ",PolSto, "mm")
                 print("Objętość tego stożka to: ",ObjSto, "mm")

             elif(Bry==Wybór_Bryły.Graniastosłup)or(Bry=="g"):
                
                Kąty=int(input("Ile kątów ma podstawa?"))
                print("WPROWADŹ NIEZBĘDNE DANE")
                A=int(input("Podaj podstawę trapezu w mm: "))
                B=int(input("Podaj drugą podstawę trapezu w mm: "))
                H=int(input("Podaj wysokość trapezu w mm: "))
                print("Podana podstawa trapezu to: ", A , "a wysokość to: ", H,"mm")
                PolTrap=( (A+B) * H / 2)
                strzałka("DÓŁ")
                print("Pole tego graniastosłupa to: ",PolTrap, "mm")
             elif(Bry==Wybór_Bryły.Prostopadłościan)or(Bry=="p"):
                print("WPROWADŹ NIEZBĘDNE DANE")
                A=int(input("Podaj długość podstawy w mm: "))
                B=int(input("Podaj drugą długość podstawy w mm: "))
                H=int(input("Podaj wysokość w mm: "))
                ab=A*B
                ah=A*H
                bh=B*H
                x=(ab+ah+bh)
                wynik=(2*x)
                    

                PolPr=(wynik)
                strzałka("DÓŁ")
                print ("Pole tego prostopadłoscianu to: ",PolPr, "mm")
                ObjPr=(A * B * H)
                print("Objętość tego prostopadłoscianu to: ",ObjPr, "mm")
                print("Wszystkie kąty wynoszą 90 stopni")
                if(A==B==H):
                        print("Ten prostopadłościan jest też sześcianem")    
             else:
                print("\n")
                print("\n")
                print("Wpisałeś coś nie tak.. zaczniemy od początku")

        else:
            print("\n")
            print("\n")
            print("Wpisałeś coś nie tak.. zaczniemy od początku")
        print("\n")
        decyzja=input("Liczymy dalej? - TAK/NIE : ")
        if(decyzja=="NIE")or(decyzja=="nie")or(decyzja=="NO")or(decyzja=="no")or(decyzja=="N")or(decyzja=="n"):
            break
        
    print("\n")
    print("\n")
    print("PROGRAM ZAKOŃCZONO")



print("używałeś klkulatora przez: ",sumowanie_czasu(kalkulator_geometryczny),"sekund")
