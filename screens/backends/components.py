class Rect:
    __UNITS = ["px", "%"]

    def __init__(self, top: str, left: str, width: str, height: str):
        self.top: str = top
        self.left: str = left
        self.width: str = width
        self.height: str = height
        self.__validate_datas()

    @staticmethod
    def __validate_data(data):
        if True not in [data.endswith(unit) for unit in Rect.__UNITS]:
            raise ValueError(f"{data} is not a valid")

    def __validate_datas(self):
        for data in [self.top, self.left, self.width, self.height]:
            Rect.__validate_data(data)


class UIComponent:
    def __init__(self, rect: Rect, id: str = None, object_class: str = None):
        self.rect = rect
        self.id = id
        self.object_class = object_class

    def __eq__(self, other):
        return self.id == other.id and self.object_class == other.object_class


class Text(UIComponent):
    def __init__(self, rect: Rect, text: str, id: str = None, object_class: str = None):
        super().__init__(rect, id, object_class)
        self.text = text


class Button(UIComponent):
    def __init__(self, rect: Rect, text: str, id: str = None, object_class: str = None):
        super().__init__(rect, id, object_class)
        self.text = text


class Entry(UIComponent):
    def __init__(self, rect: Rect, placeholder: str, id: str, object_class: str = None):
        super().__init__(rect, id, object_class)
        self.placeholder = placeholder
