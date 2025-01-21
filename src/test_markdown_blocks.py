import unittest
from markdown_blocks import markdown_to_blocks
from markdown_blocks import block_to_block_type
from markdown_blocks import markdown_to_html_node

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = '''
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type(self):
        test_md = "# This is an ideal heading!"
        self.assertEqual(block_to_block_type(test_md), "heading")
        test_md = "###### This is an ideal heading too!"
        self.assertEqual(block_to_block_type(test_md), "heading")
        test_md = "```This is a code block```"
        self.assertEqual(block_to_block_type(test_md), "code")
        test_md = "> Here's a nice quote"
        self.assertEqual(block_to_block_type(test_md), "quote")
        test_md = ">Here's another nice quote"
        self.assertEqual(block_to_block_type(test_md), "quote")
        test_md = "* This is a * unordered list"
        self.assertEqual(block_to_block_type(test_md), "unordered_list")
        test_md = "- This is a - unordered list"
        self.assertEqual(block_to_block_type(test_md), "unordered_list")
        test_md = "1. This is an ordered list"
        self.assertEqual(block_to_block_type(test_md), "ordered_list")
        test_md = "2. This is an ordered list"
        self.assertEqual(block_to_block_type(test_md), "ordered_list")
        test_md = "paragraph"
        self.assertEqual(block_to_block_type(test_md), "paragraph")

    def test_block_to_block_type_edge_cases(self):
        test_md = "####### This is not an ideal heading!"
        self.assertEqual(block_to_block_type(test_md), "paragraph")
        test_md = "```should be a code block but nope!"
        self.assertEqual(block_to_block_type(test_md), "paragraph")
        test_md = "*should be an unordered list but nope!"
        self.assertEqual(block_to_block_type(test_md), "paragraph")
        test_md = "-should be an unordered list but nope!"
        self.assertEqual(block_to_block_type(test_md), "paragraph")
        test_md = "1.should be an ordered list but nope!"
        self.assertEqual(block_to_block_type(test_md), "paragraph")
    
    def test_md_to_html_paragraph(self):
        md = '''
        this is just a simple paragraph
        '''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>this is just a simple paragraph</p></div>")

    def test_md_to_html_paragraph_2(self):
        md = '''
        this is just a simple paragraph with some **bold** text and some *italic* text!
        '''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>this is just a simple paragraph with some <b>bold</b> text and some <i>italic</i> text!</p></div>")

    def test_md_to_html_heading_para_lists(self):
        md = '''
        ## This is a 2 heading

        this is just a simple paragraph with some **bold** text and some *italic* text!

        - I also need this list!
        - And this is *important*

        1. This is an ordered list here
        2. This is another ordered list 
        '''
        node = markdown_to_html_node(md)
        html = node.to_html()
        print(f"\n\n\n\n {html}")
        self.assertEqual(html, "<div><h2>This is a 2 heading</h2><p>this is just a simple paragraph with some <b>bold</b> text and some <i>italic</i> text!</p><ul><li>I also need this list!</li><li>And this is <i>important</i></li></ul><ol><li>This is an ordered list here</li><li>This is another ordered list</li></ol></div>")

    def test_md_to_html_quotes(self):
        md = '''
        > Here is a great quote!
        > Another fantastic quote
        '''
        node = markdown_to_html_node(md)
        html = node.to_html()
        print(f"\n\n\n\n {html}")
        self.assertEqual(html, "<div><blockquote>Here is a great quote! Another fantastic quote</blockquote></div>")

    def test_markdown_to_html_node(self):
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
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it. <code>code</code> Maybe a new line here.</p><pre><code>code here!</code></pre><blockquote>a quote</blockquote><ul><li>This is the first list item in a list block</li><li>This is a <i>list</i> item</li><li>This is another list item</li></ul><ol><li>This is a list item</li><li>This is <b>another</b> list item</li></ol></div>")


if __name__ == "__main__":
    unittest.main()
