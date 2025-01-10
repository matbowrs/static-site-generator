import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_with_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual(node.url, node2.url)

    def test_not_eq_with_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        print(f"text node : {node}")
        node2 = TextNode("This is a text node", TextType.BOLD, "mcgoogle.com")
        self.assertNotEqual(node.url, node2.url)

    def test_normal_text_node_to_html_node(self):
        normal_node = TextNode("just a normal node", TextType.TEXT)
        new_leaf_node = text_node_to_html_node(normal_node)
        self.assertEqual(new_leaf_node.__repr__(), f"LeafNode(None, just a normal node, None)")

    def test_italic_text_node_to_html_node(self):
        italic_node = TextNode("italic node", TextType.ITALIC)
        new_leaf_node = text_node_to_html_node(italic_node)
        self.assertEqual(new_leaf_node.__repr__(), f"LeafNode(i, italic node, None)")

    def test_link_text_node_to_html_node(self):
        link_node = TextNode("this is a link to google", TextType.LINK, "google.com") 
        new_leaf_node = text_node_to_html_node(link_node)
        self.assertEqual(new_leaf_node.__repr__(),
                         f"LeafNode(a, this is a link to google, {{'href': 'google.com'}})")

if __name__ == "__main__":
    unittest.main()
