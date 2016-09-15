#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require ('1.9.1')

class Calc(BoxLayout):
    def __init__(self):
        super(Calc, self).__init__()

    def backspace(self, data):
        if data:
            self.display.text = data[:-1]

    def calculate(self, data):
        if not data: return
        try:
            self.display.text = str( eval(data) )
        except Exception:
            self.display.text = 'A problem has been detected...'
            #self.display.color = (0,0,1,1)


class CalcApp(App):

    def build(self):
        return Calc()

CalcApp().run()
