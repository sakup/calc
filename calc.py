#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require ('1.9.1')

class CalcLayout(BoxLayout):
    def __init__(self):
        super(CalcLayout, self).__init__()

    def backspace(self, data):
        if data:
            self.display.text = data[:-1]

    def calculate(self, data):
        if not data: return
        try:
            self.display.text = str( eval(data) )
        except Exception:
            self.display.text = 'error...'
            #self.display.color = (0,0,1,1)


class CalcApp(App):

    def build(self):
        return CalcLayout()

CalcApp().run()
