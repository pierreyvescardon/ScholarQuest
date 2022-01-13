
class Check_Answer:

    def __init__(self, reponse):
        self.reponse=reponse
        self.reponse_index=0
        self.reading= False

    def read_reponse(self):

        if self.reading:
            print (self.reponse[self.reponse_index])
            self.next_reponse()
            self.reponse_index += 1

        else:
            self.reading =True
            self.text_index=0
            print(self.reponse[self.reponse_index])

    def next_reponse(self):
        self.reponse_index += 1


        if self.reponse_index >= len(self.reponse):
            #close dialog
            self.reading=False




