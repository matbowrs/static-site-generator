import re
from textnode import TextNode
from textnode import TextType

def remove_nulls(list_type):
    list_builder = []
    for i in list_type:
        if i != '':
            list_builder.append(i)
    return list_builder

def get_special_words(txt, delimiter):
    words = []
    parts = txt.split(delimiter)
    for i in range(1, len(parts), 2):
        if i < len(parts):
            words.append(parts[i])
    
    return words

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes = []
    delim_list = []
    special_word = []

    for node in old_nodes:
        #print(f"node in split_nodes_delimiter: {node}")
        if node.text_type == TextType.TEXT:
            special_word = get_special_words(node.text, delimiter)
            #print(f"special word: {special_word}")
            if special_word:
                delim_list = node.text.split(delimiter)
                #print(f"delim_list reset: {delim_list}")
                if '' in delim_list:
                    delim_list = remove_nulls(delim_list)
                    #print(f"delim_list after nulls removed: {delim_list}")
            else:
                text_nodes.append(node)
        else:
            text_nodes.append(node)

    for word in delim_list:
        if word in special_word:
            text_nodes.append(TextNode(word, text_type, None))
        else:
            text_nodes.append(TextNode(word, TextType.TEXT, None))

    return text_nodes

def extract_markdown_images(text):
    markdown_image = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return markdown_image

def extract_markdown_links(text):
    markdown_link = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return markdown_link

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        #images_tuple = extract_markdown_links(node.text)
        #print(f"images_tuple: {images_tuple}")
        split_text = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
        split_text = remove_nulls(split_text)
        # Case for when there is just the link
        if len(split_text) == 2:
            new_nodes.append(TextNode(split_text[0], TextType.IMAGE, split_text[1]))
            break
        #print(f"split_text: {split_text}")
        for i in range(0, len(split_text), 3):
            if i+2 < len(split_text):
                print(split_text[i+1])
                print(split_text[i+2])
                new_nodes.append(TextNode(split_text[i], TextType.TEXT, None))
                new_nodes.append(TextNode(split_text[i+1], TextType.IMAGE, split_text[i+2]))
            else:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT, None))
        #print(new_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        #print(f"node.text: {node.text}")
        #links_tuple = extract_markdown_links(node.text)
        #print(f"links_tuple: {links_tuple}")
        split_text = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
        split_text = remove_nulls(split_text)
        # Case for when there is just the link
        if len(split_text) == 2:
            new_nodes.append(TextNode(split_text[0], TextType.LINK, split_text[1]))
            break
        #print(split_text)
        for i in range(0, len(split_text), 3):
            if i+2 < len(split_text):
                #print(split_text[i+1])
                #print(split_text[i+2])
                new_nodes.append(TextNode(split_text[i], TextType.TEXT, None))
                new_nodes.append(TextNode(split_text[i+1], TextType.LINK, split_text[i+2]))
            else:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT, None))
    return new_nodes

def text_to_textnodes(text):
    new_node = TextNode(text, TextType.TEXT, None)
    bolded = split_nodes_delimiter([new_node], '**', TextType.BOLD)
    italic = split_nodes_delimiter(bolded, '*', TextType.ITALIC)
    code_blocks = split_nodes_delimiter(italic, '`', TextType.CODE)
    images = split_nodes_image(code_blocks)
    links = split_nodes_link(images)
    return links

def extract_title(markdown):
    lines = markdown.split("\n")
    lines = remove_nulls(lines)
    lines = list(map(lambda x: x.strip(), lines))
    header = lines[0]
    if header.startswith("# "):
        title = header[2:]
        print(title)
        return title
    else:
        raise ValueError("Markdown does not start with <h1> (#)!")


