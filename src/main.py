import os
import shutil
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from markdown_blocks import markdown_to_blocks
from markdown_blocks import block_to_block_type
from markdown_blocks import markdown_to_html_node
from manipulate_markdown import (
    split_nodes_delimiter,
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes
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
    print(split_nodes_link([link_node]))
    image_node = TextNode("This is text with an image ![to boot dev](https://i.imgur.com/1We43fdG) and ![to youtube](https://i.imgur.com/GdfHrE2S)", TextType.TEXT)
    print(split_nodes_image([image_node]))
    link_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and a link [to youtube](https://www.youtube.com)", TextType.TEXT)
    linked_nodes = split_nodes_link([link_node])
    print(linked_nodes)
    print("--------------")
    print("--------------")
    print("--------------")
    print("TEXT_TO_TEXTNODES")
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_to_textnodes(text)
    print("--------------")
    print("--------------")
    print("--------------")
    print("MARKDOWN_TO_BLOCKS")
    md = '''
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it. ```code```
        Maybe a new line here.

        ```code here!```

        > a quote

        - This is the first list item in a list block
        - This is a *list* item
        - This is another list item

        1. This is a list item
        2. This is **another** list item
    '''
    print(f"markdown_to_blocks: {markdown_to_blocks(md)}")
    print("--------------")
    print("--------------")
    print("--------------")
    print("markdown to html node!")
    md_to_html = markdown_to_html_node(md)
    print(md_to_html.to_html())
    print("\n\n\n\n\n\n\n")
    copy_source_to_dest("/Users/matthew/workspace/github.com/matbowrs/static-site-generator/static/", "/Users/matthew/workspace/github.com/matbowrs/static-site-generator/public/") 

def setup_source_destination(src, dest):
    if os.path.exists(src) and os.path.exists(dest):
        print(f"Source path {src} and destination path {dest} exist.")
        print(f"Deleting all content under {dest}") 
        shutil.rmtree(dest)
        os.mkdir(dest)
    else:
        if not os.path.exists(src) and not os.path.exists(dest):
            print(f"Neither the source ({src}) path nor the destination path ({dest}) exist.")
        elif os.path.exists(src):
            print(f"Source path {src} exists, but destination path {dest} does not. Creating...")
            os.mkdir(dest)
            if os.path.exists(dest):
                print("Path created successfully!")
        else:
            print(f"Destination path {dest} exists, but source path {src} does not.")

def copy_source_to_dest(src, dest, src_index=0):
    src_directory_contents = os.listdir(src)
    if src_index == 0:
        setup_source_destination(src, dest)

    if len(src_directory_contents) > src_index:
        if os.path.isdir(f"{src}{src_directory_contents[src_index]}"):
            print(f"Copying dir '{src_directory_contents[src_index]}' to {dest}")
            shutil.copytree(f"{src}{src_directory_contents[src_index]}", f"{dest}{src_directory_contents[0]}")
        else:
            print(f"Copying file '{src_directory_contents[src_index]}' to {dest}")
            shutil.copy(f"{src}{src_directory_contents[src_index]}", dest)

        src_index += 1
        copy_source_to_dest(src, dest, src_index)
    else:
        print("Files copied!")
        print(f"ls {dest} -> {os.listdir(dest)}")

if __name__ == "__main__":
    main()
