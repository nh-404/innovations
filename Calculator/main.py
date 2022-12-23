import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

Window.size_hint =(0.5,0.5)
kivy.require('1.9.0')

class Bxly(BoxLayout):
    def __init__(self,**kwargs):
        super(Bxly, self).__init__()

    def calculator(self, symbol):
        self.ids.clc_field.text += symbol

    def clear(self):
        self.ids.clc_field.text = ''

    def exit(self):
        self.ids.clc_field = exit()

    def eql(self):
        self.ids.clc_field.text = str(eval(self.ids.clc_field.text))

class Calc(App):
    def build(self):
        return Bxly()

calc = Calc()
calc.run()