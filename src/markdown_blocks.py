import re
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
