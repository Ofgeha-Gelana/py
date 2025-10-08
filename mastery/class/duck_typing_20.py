from abc import ABC, abstractmethod


class TextBox():
    def draw(self):
        print("Text box")

class DropDownlist():
    def draw(self):
        print("Drop downlist")


def draw(controls):
    for control in controls:
        control.draw()

