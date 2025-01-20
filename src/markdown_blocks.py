import re
from htmlnode import HTMLNode
from textnode import TextType
from textnode import TextNode
from manipulate_markdown import split_nodes_delimiter
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
            html_nodes.append(HTMLNode(f"<h{heading_depth}>", heading_text))
        elif block_type == "paragraph":
            text_node_p = TextNode(block, TextType.TEXT)
            print(f"paragraph node: {text_node_p}")
        elif block_type == "unordered_list":
            split_items = block.split("\n")
            # Strip off any leading / ending whitespace
            split_items = list(map(lambda x: x.strip(), split_items))
            # Loop through split_items again, this time creating a new HTMLNode object 
            # For the text, remove the '*' character and just grab the text.
            unordered_nodes = list(map(lambda x: HTMLNode("<li>", get_text_from_md(x, "*")), split_items))
            print(f"unordered_nodes list {unordered_nodes}")
        elif block_type == "ordered_list":
            split_items = block.split("\n")
            # Strip off any leading / ending whitespace
            split_items = list(map(lambda x: x.strip(), split_items))
            # Loop through split_items again, this time creating a new HTMLNode object 
            # For the text, remove the '*' character and just grab the text.
            ordered_nodes = list(map(lambda x: HTMLNode("<li>", get_text_from_md(x, "*")), split_items))
            print(f"ordered_nodes list {ordered_nodes}")
    print(html_nodes)

