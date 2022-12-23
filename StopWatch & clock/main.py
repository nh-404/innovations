import kivy
from kivy.app import App
from time import strftime
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button
from  kivy.core.window import Window

Window.size_hint = (0.5,0.5)
Window.pos_hint =(0.5,0.5)
kivy.require('1.9.0')

class Clockk(App):

    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self,tick):
        self.root.ids.time.text = strftime('[size=60]%I:%M:%S %P %n [size=35]%a, %e %b %Y')

        if self.sw_started :
            self.sw_seconds += tick

        m, s = divmod(self.sw_seconds, 60)

        self.root.ids.stopWatch.text = '%02d:%02d.[size=30]%02d[/size]' % (int(m),int(s), int(s * 100 % 100))

    def stop_start(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Pause'
        self.sw_started = not self.sw_started
    
    def reset(self):
        if self.sw_started:
            self.root.ids.reset.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0

    def exit(self):
        self.root.ids.exitt.text = exit()



clockk= Clockk()
clockk.run()