from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import kivy
from kivy.core.window import Window

Window.size= (480,753)
kivy.require('1.9.0')

class Lable(Label):
    pass

class Bxly(BoxLayout):
    def __init__(self,**kwargs):
        super(Bxly,self).__init__(**kwargs)

    # def Mfss(self,symbol):
    #     self.mfs_field.text += symbol
    
    def Clear(self):
        self.mfs_field.text = ''

    def Result_BkashUssd(self):
        self.mfs_field.text = str(eval(self.mfs_field.text)*0.01875)

    def Result_BkashApp(self):
        self.mfs_field.text = str(eval(self.mfs_field.text)* 0.0175)

    def Result_BkashFav(self):
        self.mfs_field.text = str(eval(self.mfs_field.text)* 0.0149)
        
    def Result_NagadUssd(self):
        self.mfs_field.text = str(eval(self.mfs_field.text)* 0.0150)

    def Result_NagadApp(self):
        self.mfs_field.text = str(eval(self.mfs_field.text)* 0.01149)


class mfs(App):
    def build(self):
        return Bxly()

mfs().run()