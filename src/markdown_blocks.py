import re
from htmlnode import HTMLNode
from textnode import TextType
from textnode import TextNode
from manipulate_markdown import split_nodes_delimiter, text_to_textnodes
from manipulate_markdown import remove_nulls

def markdown_to_blocks(markdown):
    md = markdown.split("\n\n")
    md = list(map(lambda x: x.strip(), md))
    #for i in range(0, len(md)):
    #    if md[i][0] == "*":
    #        block = md[i].split()
    #        cleaned_block = " ".join(block)
    #        md[i] = cleaned_block
    return remove_nulls(md)

def block_to_block_type(markdown_block):
    if re.match(r"^#{1,6}(?!#)", markdown_block):
        return "heading"
    elif re.match(r"^(```.*?```)", markdown_block):
        return "code"
    elif re.match(r"^(>)", markdown_block):
        return "quote"
    elif re.match(r"^[*-] (?!\s)", markdown_block):
        return "unordered_list"
    elif re.match(r"^(\d\. )", markdown_block):
        return "ordered_list"
    else:
        return "paragraph"

def get_heading_depth(heading_text):
    list_depth = re.findall(r"^#{1,6}(?!#)", heading_text)
    return len(list_depth[0])

def get_text_from_md(text, delim):
    txt = remove_nulls(text.split(delim))
    return txt[0].strip()

def text_to_children(text):
    children_nodes = []
    text_nodes = text_to_textnodes(text)
    print(f"text_nodes: {text_nodes}") 
    for node in text_nodes:
        print(node.text_type)
        if node.text_type == TextType.BOLD:
            children_nodes.append(HTMLNode("<b>", node.text))
        elif node.text_type == TextType.ITALIC:
            children_nodes.append(HTMLNode("<i>", node.text))
        elif node.text_type == TextType.TEXT:
            children_nodes.append(HTMLNode(value=node.text))
        elif node.text_type == TextType.CODE:
            children_nodes.append(HTMLNode("<code>", node.text))
        elif node.text_type == TextType.LINK:
            children_nodes.append(HTMLNode("<a>", node.text, props={"href": node.url}))
        elif node.text_type == TextType.IMAGE:
            children_nodes.append(HTMLNode("<img>", props={"src": node.url, "alt": node.text}))
        else:
            raise TypeError("TextType is incorrect.")

    print(children_nodes)
    return children_nodes
    
def lists_to_html(text):
    children_nodes = []
    split_items = text.split("\n")

    # Strip off any leading / ending whitespace
    split_items = list(map(lambda x: x.strip(), split_items))
    # Loop through split_items again, this time creating a new HTMLNode object 
    # For the text, remove the '*' character and just grab the text.
    print(split_items)
    if "*" in split_items[0]:
        print(f"loop nodes *: {split_items}")
        list_nodes = list(map(lambda x: HTMLNode("<li>", get_text_from_md(x, "*")), split_items))
    elif "-" in split_items[0]:
        print(f"loop nodes -: {split_items}")
        list_nodes = list(map(lambda x: HTMLNode("<li>", get_text_from_md(x, "-")), split_items))
    else:
        raise ValueError("Improper list found. Please ensure lists are either ordered - or unordered *.")

    # TODO: what about ordered lists??
    # TODO: extend later for bold / italics in lists?
    return list_nodes  

def markdown_to_html(markdown):
    html_nodes = []
    blocks_list = markdown_to_blocks(markdown) 
    print(blocks_list)
    
    for block in blocks_list:
        block_type = block_to_block_type(block)
        print(block_type)
        if block_type == "heading":
            heading_depth = get_heading_depth(block)
            heading_text = get_text_from_md(block, "#")
            heading_children = text_to_children(heading_text)
            html_nodes.append(HTMLNode(f"<h{heading_depth}>", children=heading_children))
        elif block_type == "paragraph":
            children_nodes = text_to_children(block)
            html_nodes.append(HTMLNode("<p>", children=children_nodes))
        elif block_type == "unordered_list":
            print(f"unordered list!!!!!")
            unordered_list_nodes = lists_to_html(block)
            print(unordered_list_nodes)
            html_nodes.append(HTMLNode("<ul>", children=unordered_list_nodes))
        elif block_type == "ordered_list":
            ordered_list_nodes = lists_to_html(block)
            html_nodes.append(HTMLNode("<ol>", children=ordered_list_nodes))
        elif block_type == "quote":
            quote_text = get_text_from_md(block, ">")
            html_nodes.append(HTMLNode(f"<blockquote>", quote_text))
        else:
            raise TypeError("block_type does not exist")
    print(f"html nodes! {html_nodes}")
    print(HTMLNode("<div>", children=html_nodes))
    return HTMLNode("<div>", children=html_nodes)

