import pygame
from src.LuggageScreen import render_textrect

class DialogBox:

    X_POSITION = 60
    Y_POSITION = 470

    def __init__(self):

        self.box = pygame.image.load(("C:/Users/Proprio/Desktop/ScholarQuest/dialogs/dialog_box.png"))
        self.box = pygame.transform.scale(self.box, (800,150))
        self.rect = pygame.Rect(40,40,400,100)
        self.texts = []
        self.text_index = 0
        self.question=[]
        self.letter_index = 0# pour afficher les lettres 1 par 1
        self.font = pygame.font.Font("C:/Users/Proprio/Desktop/ScholarQuest/dialogs/dialog_font.ttf", 12)#18 correspond q lq tqille de la police
        self.reading = False

    def execute(self, dialog=[], question=[]):
        if self.reading:
            self.next_text()#si je suis en mode lecture je pourrais passer a la prochaine phrase
        else:
            self.reading =True
            self.text_index=0
            self.texts = dialog
            self.question=question
            self.question.insert(0,"")#ajoute un décalage necessaire entre les questions et les reponses

    #def render_text(self):
#refaire le def render mais avec le rect
    def render(self, screen):
        if self.reading:
            self.letter_index +=1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index =self.letter_index

            screen.blit(self.box, (self.X_POSITION,self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0,0,0))# permet d'avoir la couleur noire
            screen.blit(text, (self.X_POSITION +60, self.Y_POSITION + 30))#permet de positionner le texte
            #render_textrect("pourquoi ne pas ecrire plein de texte pour cette verification ce serait une bonne idee",self.font,self.rect, (48, 48, 48), 0)

    def next_text(self):
        self.text_index += 1
        self.letter_index=0

        if self.text_index >= len(self.texts):
            #close dialog
            self.reading=False



