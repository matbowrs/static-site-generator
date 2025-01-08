import unittest
from htmlnode import LeafNode 

class TestHTMLNode(unittest.TestCase):
    def test_leaf_node(self):
        leaf_node_p = LeafNode("p", "Some text to render!")
        self.assertEqual(leaf_node_p.tag, "p")
        self.assertEqual(leaf_node_p.value, "Some text to render!")

    def test_leaf_node_props(self):
        leaf_node_a = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(leaf_node_a.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
if __name__ == "__main__":
    unittest.main()
