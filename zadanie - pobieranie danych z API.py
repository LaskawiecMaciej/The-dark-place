#zadanie: spróbuj z publicznego api: jsonplaceholder/todos pobrać dane dotyczące wykonanych zadań przez użytkowników, a następnie przydziel nagrodę 2 najlepszym z nich




import json
import requests


#FUNKCJA TESTUJĄCA WSTĘPNIE STRONĘ

def check_site (siteAdress):
    response=requests.get(siteAdress)
    if(response.status_code==200):
        print("SITE OPENED SUCCESFULLY")
        return(response)
    else:
        print("UNFORTUNETTLY THE PROBLEM ACCURED WHILE TRIED TO GET SITE FILES. \n PAGE IS BEING ADDED TO ARCHIVE FILE NOW.")
        with open("nieotwarte strony.txt", "w", encoding="UTF-8")as file:
            file.write(f"PAGE: {siteAdress} CANNOT BE OPENED BECAUSE OF {response.status_code} ERROR. ")
        return(response)

#FUNKCJA ZMIENIAJĄCA RESPONSE STRONY W STRING TYPU JSON

def site_to_json_string_converter(site_response):
    try:
        convertedSite=json.loads(site_response.text)
        return(convertedSite)
    except json.decoder.JSONDecodeError:
        print("THERE ARE ISSUES WITH PAGE RESPONSE GIVEN \nMAKE SHURE PAGE IS IN A JSON READABLE FORMAT")


#  TERAZ SPRÓBUJEMY UTWORZYĆ SŁOWNIK PODAJĄCY INFORMACJE O WYKONANYCH PRZEZ
#  PRACOWNIKÓW ZADANIACH


#FUNKCJA TWORZĄCA LISTĘ UŻYTKOWNIKÓW O NAJWYŻSZYCH WYNIKACH
def users_with_best_results(dictionary):
    return[
        key
        for (key, value) in dictionary.items()
        if value == max(dictionary.values()) ]
            
    
    
#FUNKCJA TWORZĄCA SŁOWNIK Z ID PRACOWNIKA ORAZ ILOŚCIĄ WYKONANYCH ZADAŃ
def list_of_employes_Scores(employesScoresList):
    emptyDict=dict()

    for key in employesScoresList:
        if(key['completed']==True):
            try:
                emptyDict[key["userId"]]+=1
            except KeyError:
                emptyDict[key["userId"]]=1
    return(emptyDict)


tekst=site_to_json_string_converter(check_site("https://jsonplaceholder.typicode.com/todos"))

#print(list_of_employes_Scores(tekst))

wygraniUżytkownicy=users_with_best_results(list_of_employes_Scores(tekst))

Users=site_to_json_string_converter(check_site("https://jsonplaceholder.typicode.com/users"))

#tu szukamy dane użytkowników

for user in Users:
    if user["id"] in wygraniUżytkownicy:
        print("nagroda przypadnie", user["name"])
"""

#ta funkcja bierze id z listy wygranych i zmienia je w string do adresu url

def list_to_conected_parameters(lista):
    connection=("id=")
    users=""
    x=len(lista)
    i=0
    for key in lista:
        i+=1
        if(i==x):
            user=(connection+str(key))
        else:
            user=(connection+str(key)+"&")
        users+=user

    return(str(users))
    
#listaMoja=[1,3,5,7]
użytkownik1=requests.get("https://jsonplaceholder.typicode.com/users/?"+(list_to_conected_parameters(wygraniUżytkownicy)))

pracownik = użytkownik1.json()
print(pracownik)
#for key in pracownik:
   # print("Wręczamy nagrodę dla użytkowników: ",pracownik[key]["name"])
"""
