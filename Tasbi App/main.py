from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import StringProperty

class dm(GridLayout):

    count = 0
    count_en =False
    myStr= StringProperty('0')

    count2 = 0
    count_en2 =False
    myStr2= StringProperty('0')

    count3 = 0
    count_en3 =False
    myStr3= StringProperty('0')

    myStr4= StringProperty('0')

    def onClick(self):
        
        if self.count_en:
            self.count+=1
            self.myStr= str(self.count)
            self.myStr4= str(self.count+self.count2+self.count3)


    def onClick2(self):

        if self.count_en2:
            self.count2 +=1
            self.myStr2= str(self.count2)
            self.myStr4= str(self.count+self.count2+self.count3)


    def onClick3(self):

        if self.count_en3:
            self.count3 +=1
            self.myStr3= str(self.count3)
            self.myStr4= str(self.count+self.count2+self.count3)


    def tggl(self,widget):

        if widget.state == 'normal':
            widget.text='off'
            self.count_en=False

        else:
            widget.text='on'
            self.count_en=True


    def tggl2(self,widget2):

        if widget2.state == 'normal':
            widget2.text='off'
            self.count_en2=False

        else:
            widget2.text='on'
            self.count_en2=True


    def tggl3(self,widget3):

        if widget3.state == 'normal':
            widget3.text='off'
            self.count_en3=False

        else:
            widget3.text='on'
            self.count_en3=True


                



class lb(Label):
    pass

class demo(App):
    pass

demo().run()