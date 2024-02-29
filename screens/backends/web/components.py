from screens.backends.components import *
import pyodide_html as html
import js
from abc import abstractmethod

ROOT_DIV = "app"


class IWebComponent(UIComponent):
    @abstractmethod
    def _init_native_component(self):
        raise NotImplementedError

    def draw(self):
        element = self._init_native_component()
        element.add(style=f"position: absolute; top: {self.rect.left}; left: {self.rect.top}; width: {self.rect.width}; height: {self.rect}")
        if self.id is not None:
            element.add(id=self.id)
        if self.object_class is not None:
            element.add(className=self.object_class)
        print(js.document.getElementById(ROOT_DIV))
        js.document.getElementById(ROOT_DIV).appendChild(element)


class WebText(Text, IWebComponent):
    def __init__(self, rect: Rect, text: str, id: str=None, object_class: str=None):
        super().__init__(rect, text, id, object_class)

    def _init_native_component(self):
        return html.p(self.text)


class WebButton(Button, IWebComponent):
    def __init__(self, rect: Rect, text: str, id: str=None, object_class: str=None):
        super().__init__(rect, text, id, object_class)

    def _init_native_component(self):
        return html.button(self.text)
