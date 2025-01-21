import re
from htmlnode import ParentNode
from textnode import text_node_to_html_node
from manipulate_markdown import text_to_textnodes
from manipulate_markdown import remove_nulls

def markdown_to_blocks(markdown):
    md = markdown.split("\n\n")
    md = list(map(lambda x: x.strip(), md))
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

def get_text_from_md(text, delim):
    txt = remove_nulls(text.split(delim))
    return txt[0].strip()

def text_to_children(text):
    children_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children_nodes.append(html_node)
    print(f"text_to_children: {children_nodes}")
    return children_nodes
    
def get_heading_depth(heading_text):
    list_depth = re.findall(r"^#{1,6}(?!#)", heading_text)
    return len(list_depth[0])

def block_to_heading(block):
    heading_depth = get_heading_depth(block)
    heading_text = get_text_from_md(block, "#")
    heading_children = text_to_children(heading_text)
    #print(ParentNode(f"<h{heading_depth}>", heading_children))
    return ParentNode(f"h{heading_depth}", heading_children)

def block_to_paragraph(block):
    #print("block to paragraph")
    #print(block)
    split_block = block.split("\n")
    split_block = list(map(lambda x: x.strip(), split_block))
    #print(split_block)
    paragraph_children = " ".join(split_block)
    paragraph_children = text_to_children(paragraph_children)
    print(ParentNode("p", paragraph_children))
    return ParentNode("p", paragraph_children)

def block_to_code(block):
    print("block to code")
    code_text = get_text_from_md(block, "```")
    print(code_text)
    code_children = text_to_children(code_text)
    code_node = ParentNode("code", code_children)
    return ParentNode("pre", [code_node])

def block_to_quote(block):
    print(f"block to quote: {block}")
    if block.startswith(">"):
        quote_text = get_text_from_md(block, ">")
        print(quote_text)
        quote_text = text_to_children(quote_text) 
        print(quote_text)
        return ParentNode("blockquote", quote_text)
    else:
        raise ValueError("> is not the beginning of the line.")

def block_to_ul(block):
    print("block to ul")
    lines = block.split("\n")
    list_items = []
    for line in lines:
        # Disregard the * or - , we just want the text
        line = line.strip()
        text = line[2:]
        print(f"ul text: {text}")
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)

def block_to_ol(block):
    print("block to ol")
    lines = block.split("\n")
    list_items = []
    for line in lines:
        # Disregard the 1. 2. , etc. 
        line = line.strip()
        text = line[3:]
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)

def block_to_html_node(block):
    print("block to html node")
    print(block)
    block_type = block_to_block_type(block)
    if block_type == "heading":
        return block_to_heading(block)
    if block_type == "paragraph":
        return block_to_paragraph(block)
    if block_type == "code":
        return block_to_code(block)
    if block_type == "ordered_list":
        return block_to_ol(block)
    if block_type == "unordered_list":
        return block_to_ul(block)
    if block_type == "quote":
        return block_to_quote(block)
    raise ValueError("Block type is incorrect")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    print(ParentNode("div", children=children))
    return ParentNode("div", children=children)

