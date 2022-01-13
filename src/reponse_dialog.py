import pygame

class Reponse_DialogBox:

    X_POSITION = 60
    Y_POSITION = 120

    def __init__(self):

        self.box = pygame.image.load(("C:/Users/Proprio/Desktop/ScholarQuest/dialogs/dialog_box.png"))
        self.box = pygame.transform.scale(self.box, (700,100))
        self.reponse_player = str
        self.input_text = ""
        self.font = pygame.font.Font("C:/Users/Proprio/Desktop/ScholarQuest/dialogs/dialog_font.ttf", 12)
        self.reading = False


    def execute(self):
        if self.reading :
           self.next_questions()

        else:
            self.reading=True
            self.input_text="entrez votre reponse : "






    def render(self, screen):
        if self.reading:

            screen.blit(self.box, (self.X_POSITION,self.Y_POSITION))
            text = self.font.render(self.input_text, False, (0,0,0))# permet d'avoir la couleur noire
            screen.blit(text, (self.X_POSITION +60, self.Y_POSITION + 30))#permet de positionner le texte

    def next_questions(self):
        self.reponse_player=self.input_text
        self.input_text=""


