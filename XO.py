from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

choice = ["0", "X"]
switch = 1

class Tic_Tac_Toe(App):

    def game_over(self, win):
        global switch
        if not switch:
            self.player.text = "X wins"
        else:
            self.player.switch = "0 wins"
        for i in range(9):
            self.buttons[i].disabled = True
        for i in win:
            self.buttons[i].color = [0, 1, 0, 1]


    def build(self):
        admin = BoxLayout(orientation="vertical")
        self.player = Label(size_hint=[1, 0.1], font_size=40, text="X")
        root = GridLayout(cols=3)
        self.buttons=[]
        for i in range(9):
            self.buttons.append(Button(font_size=40, text="", on_press=self.Game, background_color=[1, 1, 2, 3]))
        for i in range(9):
            root.add_widget(self.buttons[i])
        restart = Button(text="Restart", on_press=self.Restart, font_size=40, size_hint=[1, 0.1])
        admin.add_widget(self.player)
        admin.add_widget(root)
        admin.add_widget(restart)
        return admin
    def Game(self, button):
        wins = [[0,1,2], [3,4,5,], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        global switch
        button.text = choice[switch]
        button.disabled = True
        if switch == 0:
            switch = 1
        else:
            switch = 0
        self.player.text = choice[switch]
        for i in wins:
            win = 0
            if self.buttons[i[0]].text == self.buttons[i[1]].text == self.buttons[i[2]].text == "X" or \
                    self.buttons[i[0]].text == self.buttons[i[1]].text == self.buttons[i[2]].text == "0":
                self.game_over(i)




    def Restart(self, button):
        for i in range(9):
            self.buttons[i].disabled = False
            self.buttons[i].text=""
            self.player.text="X"

Game = Tic_Tac_Toe()
Game.run()


