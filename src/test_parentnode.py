import unittest
from htmlnode import ParentNode , LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_node(self):
        parent_node = ParentNode(
        "p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(parent_node.tag, "p")
        self.assertNotEqual(parent_node.children, None)

    def test_parent_node_repl(self):
        parent_node = ParentNode("p", [LeafNode("b", "Bold text")], None)
        self.assertEqual(parent_node.__repr__(), "ParentNode(p, [LeafNode(b, Bold text, None)], None)")

    def test_parent_node_children(self):
        parent_node = ParentNode("p", [LeafNode("b", "Bold text")], None)
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b></p>")

    def test_parent_node_many_children(self):
        parent_node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "normal text"),
            LeafNode("i", "italic text"),
            LeafNode("code", "code text")
        ], None)
        self.assertEqual(parent_node.to_html(), 
                         "<p><b>Bold text</b>normal text<i>italic text</i><code>code text</code></p>")
    
    def test_parent_node_no_children(self):
        parent_node = ParentNode("p", [], None)
        with self.assertRaises(ValueError):
            parent_node.to_html() 

    def test_parent_node_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("b", "Bold text")], None)
        with self.assertRaises(ValueError):
            parent_node.to_html() 


if __name__ == "__main__":
    unittest.main()
