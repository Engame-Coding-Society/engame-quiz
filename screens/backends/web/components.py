from screens.backends.components import *
from abc import abstractmethod


class IWebComponent(UIComponent):
    @abstractmethod
    def _get_beginning(self):
        raise NotImplementedError

    @abstractmethod
    def _get_content(self):
        raise NotImplementedError

    @abstractmethod
    def _get_end(self):
        raise NotImplementedError

    @abstractmethod
    def _get_type(self):
        raise NotImplementedError

    def generate(self):
        element = self._get_beginning()
        if self.id is not None:
            element += f" id=\"{self.id}\""
        if self.object_class is not None:
            element += f" class=\"{self.object_class}\""
        element += f" style=\"position: absolute; top: {self.rect.left}; left: {self.rect.top}; width: {self.rect.width}; height: {self.rect.height}\""
        element += self._get_content()
        element += self._get_end()
        return {"id": self.id, "content": element, "type": self._get_type()}


class WebText(Text, IWebComponent):
    def __init__(self, rect: Rect, text: str, id: str=None, object_class: str=None):
        super().__init__(rect, text, id, object_class)

    def _get_beginning(self):
        return "<p"

    def _get_content(self):
        return f">{self.text}"

    def _get_end(self):
        return "</p>"

    def _get_type(self):
        return "text"


class WebButton(Button, IWebComponent):
    def __init__(self, rect: Rect, text: str, id: str=None, object_class: str=None):
        super().__init__(rect, text, id, object_class)

    def _get_beginning(self):
        return "<button type=\"button\""

    def _get_content(self):
        return f">{self.text}"

    def _get_end(self):
        return "</button>"

    def _get_type(self):
        return "button"


class WebEntry(Entry, IWebComponent):
    def __init__(self, rect: Rect, placeholder: str=None, id: str=None, object_class: str=None):
        super().__init__(rect, placeholder, id, object_class)

    def _get_beginning(self):
        return "<input type=\"text\""

    def _get_content(self):
        return f" placeholder=\"{self.placeholder}\""

    def _get_end(self):
        return "/>"

    def _get_type(self):
        return "entry"