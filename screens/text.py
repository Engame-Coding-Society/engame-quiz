import pygame_gui
from pygame import Rect


class Text:
    def __init__(self, rect: Rect, text: str, manager: pygame_gui.UIManager):
        self.rect = rect
        self.manager = manager
        self.labels = []
        rows = text.splitlines()
        label_height = int(self.rect.height // len(rows))
        for ri in range(len(rows)):
            self.labels.append(pygame_gui.elements.UILabel(
                Rect(self.rect.left, self.rect.top + ri * label_height, self.rect.width, label_height),
                rows[ri], manager=self.manager))
