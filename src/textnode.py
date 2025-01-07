from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold" 
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        # Verify text_type passed is of type TextType(Enum) 
        if not isinstance(text_type, TextType):
            print(f"text_type arg is not a valid enum")
            raise TypeError(f"Expected TextType(Enum). Got {type(text_type)}")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNodeObj):
        return (
            self.text == TextNodeObj.text
            and self.text_type == TextNodeObj.text_type
            and self.url == TextNodeObj.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
