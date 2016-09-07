import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require ("1.9.1")

class MyWindowApp(App):
    def build(self):
        lbl = Label(text='WTF')
        return lbl

window = MyWindowApp()
window.run()

#comment
#comment2
