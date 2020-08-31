import cv2
import numpy as np
import MouseClicks as MC
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Buttons(App):
    def build(self):
        layoutsize = ((300,300))
        layout = FloatLayout(size=(layoutsize))

        button1 = Button(text="Function 1", size_hint=(.1, .1),
                         pos_hint={'x':.1, 'y':.9})

        
        button2 = Button(text="Function 2", size_hint=(.1, .1),
                         pos_hint={'x':.1, 'y':.8})
        
        button1.bind(on_press=self.press1)
        button2.bind(on_press=self.press2)
        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout
    def press1(self,instance):
        MC.test()
    def press2(self,instance):
        print("kakkosfunc")


def main():
    Buttons().run()


if __name__ == "__main__":
    main()