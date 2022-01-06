# -*- coding: utf-8 -*-

import csv
import time
import random

class questionnaire:

    def __init__(self,name):
        tableauCSV = csv.DictReader(open(f"C:/Users/Proprio/Desktop/ScholarQuest/{name}.csv", 'r', encoding='utf-8-sig'))
        Dictionnaire = [dict(row) for row in tableauCSV]
        self.questions = []
        self.reponse = []

        for i in Dictionnaire:  # Dictionnaire est une liste de dictionnaires qui contiennent pour chacun une réponse et une question associées (clef:Question et clef:Reponse)
            self.questions.append(i["Question"])
            self.reponse.append(i["Reponse"])





#a.ListeQuestions(name="Questions")
#print(a.reponse)
