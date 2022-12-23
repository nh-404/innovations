from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
from time import strftime
from kivymd.uix.floatlayout import MDFloatLayout
import datetime

Window.size_hint= (0.6,0.7)
Window.pos_hint=( 0.5,0.5 )

# class Md(MDFloatLayout):
#         def __init__(self,**kwargs):
#          super(Md,self).__init__(**kwargs)

#         def time_picker(self):
#             time_dialog= MDTimePicker()
#             time_dialog.bind(time=self.get_time, on_save= self.schedule)
#             time_dialog.open()
#         def get_time(self,instance,time):
#             print(time)
kv = ''' 

MDFloatLayout:
    md_bg_color: 1,1,1,1
    MDLabel:
        text: 'Alarm'
        pos_hint: {'center_y':0.935}
        halign: 'center'
        bold: True
    MDIconButton:
        icon: 'plus'
        pos_hint: {'center_x': 0.87, 'center_y':0.94}
        md_bg_color: 0,0,0,1
        theme_text_color: 'Custom'
        text_color:1,1,1,1
        on_release: app.time_picker()
    MDLabel:
        id: alarm_time
        text: ''
        pos_hint: {'center_y': 0.5}
        font_size: '30sp'
        bold: True
    # MDRaiseButton:
    #     text: 'stop'
    #     pos_hint: {'center_x': 0.5 ,'center_y': 0.4}
         

'''

class Stopwatch(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def time_picker(self):
        time_dialog= MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save= self.schedule)
        time_dialog.open()
    def get_time(self,instance,time):
        print(time)

    def schedule(self,**args):
        pass
        

stopwatch = Stopwatch()

stopwatch.run()