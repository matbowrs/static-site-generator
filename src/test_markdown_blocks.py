import unittest
from markdown_blocks import markdown_to_blocks
from markdown_blocks import block_to_block_type

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

if __name__ == "__main__":
    unittest.main()
