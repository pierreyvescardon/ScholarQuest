import os
import csv


#ouverture du fichier CSV contenant les chemins à vérifier

file = open("C:/Users/Proprio/Desktop/essai.csv", 'r', encoding='utf-8-sig')
csv_reader = csv.reader(file)
lists_from_csv = []
Lists_path=[]

# ajout des lignes du csv dans une liste en supprimant les erreurs de formatage entrainant du texte avant l'indication de la racine C du chemin
for row in csv_reader:
    if (row[0].find("C")>-1):
        lists_from_csv.append(((row[0])[row[0].index("C"):]))
    else:
        lists_from_csv.append(row[0]) #le [0] est nécessaire car chaque ligne récupérée depuis csv.reader est une liste de 1 élément

#on récupere les élémets de la précédente liste dans une nouvelle liste pour remplacer le formatage des backslash par des slashs
for line in lists_from_csv:
    Lists_path.append((line.replace("\\","/")))
print(Lists_path)

#vérification si les chemins indiqué dans la liste existe bien.
for element in Lists_path:
    if os.path.exists(element) == False:
        print(f"{element} n'a pas été livré")
    else:
        print(f"{element} a été livré")


