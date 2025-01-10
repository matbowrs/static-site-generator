from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold" 
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise TypeError("Unknown TextType was passed!")
