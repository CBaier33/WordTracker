import kivy
import time
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty, ColorProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.clock import Clock
from pocketsphinx import LiveSpeech

class tracker(Widget):
   
    def __init__(self, **kwargs):
        super(tracker, self).__init__(**kwargs)
        self.word_count = 0
        self.toggled = False
        Clock.schedule_interval(self.update, 1.0/60.0)
        print(self.start_stop.center_x)
    def update(self, dt):
        if self.toggled == True:
            self.loop()

    def loop(self):
        i = 0
        dict= {}
        for phrase in LiveSpeech():
            if i > 1:
                break
            i += 1
            text = str(phrase)
            sentence = text.split(' ')
            for word in sentence:
                self.word_count += 1
                dict[word] = 1 + dict.get(word, 0)
            print(f'Total word count: {self.word_count}')
            self.word_counter.text = str(self.word_count)

    def toggle(self):
        
        if self.start_stop.state == 'normal':
            self.start_stop.text = "Start"
            self.start_stop.background_color = (0,204/255, 0, 1)
            self.toggled = False

        else:
            self.start_stop.text = "Stop"
            self.start_stop.background_color = (1,0,0,1)
            self.toggled = True

class WordTrackerApp(App):
    def build(self):
        tr = tracker()
        return tracker()

if __name__ == '__main__':
    WordTrackerApp().run()
