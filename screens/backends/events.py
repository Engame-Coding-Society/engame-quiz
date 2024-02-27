from enum import Enum


class EventType(Enum):
    BUTTON_PRESSED = "button_pressed",
    ENTRY_VALUE_CHANGED = "entry_value_change"


class Event:
    # TODO: Should have the :param: component a UI component type
    def __init__(self, type: EventType, component):
        self.type = type
        self.component = component


class ButtonPressedEvent(Event):
    def __init__(self, component):
        super().__init__(EventType.BUTTON_PRESSED, component)


class EntryValueChangedEvent(Event):
    def __init__(self, component, value):
        super().__init__(EventType.ENTRY_VALUE_CHANGED, component)
        self.value = value
