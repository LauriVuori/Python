import cv2
import numpy as np
from kivy.app import App
from kivy.uix.button import Button

class Buttons(App):
    def build(self):
        button = Button(text="Function 1", pos=(25,400), size_hint = (.25, .18))
        button.bind(on_press=self.press)
        return button
    def press(self,instance):
        print("Pressed")




def main():
    Buttons().run()


if __name__ == "__main__":
    main()