from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode

def main():
    # Text Nodes
    test_node = TextNode("test node", TextType.ITALIC, "google.com")
    print(f"test_node: {test_node}")
    test_node_two = TextNode("test node", TextType.ITALIC, "google.com")
    print(f"test_node_two: {test_node}")
    print(f"nodes equal? -> {test_node == test_node_two}")

    # HTML Nodes
    html_node_attr = {"href":"https://www.google.com","target":"_blank"}
    html_node = HTMLNode(props=html_node_attr)
    html_node.props_to_html()
    print(html_node)
if __name__ == "__main__":
    main()
