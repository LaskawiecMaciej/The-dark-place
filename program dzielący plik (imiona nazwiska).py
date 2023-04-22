# ten program po prostu pobiera imiona i nazwiska z pliku po czym zapisuje je do dwóch plików - jednego z imionami i drugiego z nazwiskami

with open("imiona i nazwiska.txt" , "r" , encoding="UTF-8") as file:

    tekst=file.read().splitlines()
    
    names=[item.split(" ")[0]for item in tekst ]
    surnames=[item.split(" ")[1]for item in tekst]
imiona=(' '.join(names))
nazwiska=(' '.join(surnames))
with open("imiona.txt" , "w",encoding="UTF-8") as file:
    file.write(imiona)

with open("nazwiska.txt" , "w",encoding="UTF-8") as file:
    file.write(nazwiska)
