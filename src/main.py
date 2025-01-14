from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from manipulate_markdown import (
    split_nodes_delimiter,
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image
)

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

    # SPLIT
    print("--------------")
    print("--------------")
    print("--------------")
    print("--------------")
    print("SPLIT")
    node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(f"new_nodes double bold **: {new_nodes}")

    print("EXTRACT")
    print("--------------")
    print("--------------")
    print("--------------")
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    print("--------------")
    print("--------------")
    print("--------------")
    print("NODE LINK/IMAGE EXTRACT")
    link_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
    image_node = TextNode("This is text with an image ![to boot dev](https://i.imgur.com/1We43fdG) and ![to youtube](https://i.imgur.com/GdfHrE2S)", TextType.TEXT)
    print(split_nodes_link([link_node]))
    print(split_nodes_image([image_node]))
if __name__ == "__main__":
    main()
