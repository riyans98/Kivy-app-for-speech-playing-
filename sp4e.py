from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

import os 
import random
from time import time

class Main(RelativeLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.player = Player()

        playbutton = Button(
            text = "Play",
            size_hint = (.1, .1),
            pos_hint = {"center_x": 0.4, "center_y": 0.3},
            on_press = self.player.play)

        stopbutton = Button(
            text = "Stop",
            size_hint = (.1, .1),
            pos_hint = {"center_x": 0.6, "center_y": 0.3},
            on_press = self.player.stop)
    
        self.add_widget(playbutton)
        self.add_widget(stopbutton)

class MyApp(App):
    def build(self):
        return Main()


class Player:
    def __init__(self):
        
        self.song = SoundLoader.load('speech.mp3')
        self.pos = 0
        self.start_time = None
        self.stop_time = 0
        self.stopped_time = None

    def mix_playlist(self):
        mixedPlaylist = []
        while len(self.playlist) > 0:
            item = random.choice(self.playlist)
            mixedPlaylist.append(item)
            self.playlist.remove(item)
        self.playlist = mixedPlaylist

    def t(self):
        if self.start_time is None:
            self.start_time = time()

        return int(time() - self.start_time - self.stop_time)

    def s(self):
        if self.stopped_time:
            self.stop_time += time() - self.stopped_time
    def play(self, _):
    	if self.song.state == "stop":
        	self.song.play()
        	if self.pos > 0:
        		Clock.schedule_once(self.unpause,0)
    def unpause(self, _):
    	self.song.seek(self.pos)


    def stop(self, _):
        self.pos = self.song.get_pos()
        self.song.stop()
        self.stopped_time = time()

app = MyApp()
app.run()

