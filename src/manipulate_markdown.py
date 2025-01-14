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
        #print(f"node: {node}")
        if node.text_type == TextType.TEXT:
            special_word = get_special_words(node.text, delimiter)
            #print(f"special word: {special_word}")
            delim_list = node.text.split(delimiter)
        else:
            text_nodes.append(node)

    #print(f"delim_list reset: {delim_list}")
    if '' in delim_list:
        delim_list = remove_nulls(delim_list)

    #print(f"delim_list after nulls removed: {delim_list}")
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
        images_tuple = extract_markdown_links(node.text)
        images_dict = dict(images_tuple)
        split_text = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
        split_text = remove_nulls(split_text)
        for text in split_text:
            if text in images_dict:
                new_nodes.append(TextNode(text, TextType.LINK, images_dict[text]))
            elif text not in images_dict.values():
                new_nodes.append(TextNode(text, TextType.TEXT, None))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links_tuple = extract_markdown_links(node.text)
        #print(f"links_tuple: {links_tuple}")
        links_dict = dict(links_tuple)
        # Split the text on the regex used in the function above
        # This makes it easier to parse out what will be a
        # TextType.LINK and a TextType.TEXT type
        split_text = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
        split_text = remove_nulls(split_text)
        #print(f"split_text: {split_text}")
        for text in split_text:
            if text in links_dict:
                new_nodes.append(TextNode(text, TextType.LINK, links_dict[text]))
            elif text not in links_dict.values():
                new_nodes.append(TextNode(text, TextType.TEXT, None))

    return new_nodes
