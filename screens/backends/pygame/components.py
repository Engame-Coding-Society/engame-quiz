from screens.backends.components import Text, Button, Entry
import pygame_gui
from screens.backends.pygame.constants import SCREEN_SIZE
from screens.backends import components
from pygame import Rect
from pygame_gui import UIManager


def convert_percentages(component: str, screen_scale: float) -> float:
    return (float(component.split("%")[0]) / 100) * screen_scale


def convert_unit(component: str, screen_scale: float) -> float:
    return convert_percentages(component, screen_scale) if "%" in component else float(component.split("px")[0])


def to_pygame_rect(rect: components.Rect) -> Rect:
    return Rect(convert_unit(rect.top, SCREEN_SIZE[0]), convert_unit(rect.left, SCREEN_SIZE[1]),
                convert_unit(rect.width, SCREEN_SIZE[0]), convert_unit(rect.height, SCREEN_SIZE[1]))


class PygameText(Text):
    def __init__(self, ui_manager: UIManager, rect: components.Rect, text: str,
                 id: str=None, object_class: str=None):
        super().__init__(rect, text, id, object_class)
        self.labels = []
        native_rect = to_pygame_rect(self.rect)
        rows = text.splitlines()
        label_height = int(native_rect.height // len(rows))
        for ri in range(len(rows)):
            self.labels.append(pygame_gui.elements.UILabel(
                Rect(native_rect.left, native_rect.top + ri * label_height, native_rect.width, label_height),
                rows[ri], manager=ui_manager))


class PygameButton(Button):
    def __init__(self, ui_manager: UIManager, rect: components.Rect, text: str,
                 id: str=None, object_class:str=None):
        super().__init__(rect, text, id, object_class)
        pygame_gui.elements.UIButton(to_pygame_rect(self.rect), self.text, ui_manager,
                                     object_id=pygame_gui.core.ObjectID(object_id=self.id, class_id=self.object_class))


class PygameEntry(Entry):
    def __init__(self, ui_manager: UIManager, rect: components.Rect, placeholder: str,
                 id: str=None, object_class: str=None):
        super().__init__(rect, placeholder, id, object_class)
        pygame_gui.elements.UITextEntryLine(to_pygame_rect(self.rect), manager=ui_manager,
                                            placeholder_text=self.placeholder, object_id=pygame_gui.core.ObjectID(
                                            object_id=self.id, class_id=self.object_class))
