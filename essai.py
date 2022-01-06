# -*- coding: utf-8 -*-

import csv
import time
import random

tableauCSV = csv.DictReader(open("Questions.csv", 'r', encoding='utf-8-sig'))
Dictionnaire = [dict(row) for row in tableauCSV]

random.shuffle(Dictionnaire) #Melange les dictionnaires comopsant la liste de dictionnaire de la variable Dictionnaire en la modifiant directement (pas besoin de la rediriger vers une autre variable)

#Ce petit programme consiste en jeu pour retenir plus facilement les commandes de bases linux
vies = 3
reponse="rien"
score=0

for i in Dictionnaire: # Dictionnaire est une liste de dictionnaires qui contiennent pour chacun une réponse et une question associées (clef:Question et clef:Reponse)
    print(i["Question"]+"\n")
    begin=int(time.perf_counter())
    reponse= input("Votre reponse : ")
    while reponse != i["Reponse"]:
        vies-= 1
        print("Ce n'est pas la bonne réponse. Il te reste {} vies".format(vies))
        if vies > 0 :
            reponse = input("Votre reponse : ")
        else :
            print("GAMEOVER")
            print("vous avez {} points".format(score))
            exit()
    end=int(time.perf_counter())
    if ((30-(end-begin))>0):
        score=score+(30-(end-begin))
    else : score=score
    print("Vous avez {} points".format(score))
print("Bien joué, c'est gagné. vous obtenez le score finale de {} points".format(score))

