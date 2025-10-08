from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("Text box")

class DropDownlist(UIControl):
    def draw(self):
        print("Drop downlist")


def draw(controls):
    for control in controls:
        control.draw()

