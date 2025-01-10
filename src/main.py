from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

    # Leaf Nodes
    leaf_node_p = LeafNode("p", "Some text to render!")
    print(f"leaf_node_p: {leaf_node_p.to_html()}")
    leaf_node_a = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
    print(f"leaf_node_a to_html(): {leaf_node_a.to_html()}")
    print(f"leaf_node_a: {leaf_node_a}")

    # Parent Nodes:
    parent_node = ParentNode(
        "p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(f"parent node -> {parent_node.__repr__()}")
    print(parent_node)
    print(f"attempt to use to_html")
    parent_node.to_html()
    print("--------------")
    print("TextNode -> HTMLNode")
    print(text_node_to_html_node(test_node))
if __name__ == "__main__":
    main()
