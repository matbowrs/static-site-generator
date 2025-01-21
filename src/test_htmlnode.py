import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        html_node_attr = {"href":"https://www.google.com","target":"_blank"}
        html_node = HTMLNode("p", "new html node", None, props=html_node_attr)
        print(html_node)
        self.assertEqual(f'HTMLNode(p, new html node, None, {html_node_attr})', repr(html_node))
        #self.assertEqual(repr(html_node), "HTMLNode(p, new html node, None, {href=})")

    def test_props_to_html(self):
        html_node_attr = {"href":"https://www.google.com","target":"_blank"}
        html_node = HTMLNode(props=html_node_attr)
        html_node_props_to_html = html_node.props_to_html()
        self.assertEqual(f' href="https://www.google.com" target="_blank"', html_node_props_to_html)

    def test_html_node_values(self):
        html_node_attr = {"href":"https://www.google.com","target":"_blank"}
        html_node = HTMLNode("p", "new html node", None, props=html_node_attr)
        self.assertEqual(html_node.tag, "p")
        self.assertEqual(html_node.value, "new html node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, html_node_attr)

    def test_html_node_children(self):
        html_node_attr = {"href":"https://www.google.com","target":"_blank"}
        html_node_child = HTMLNode("p", "new html node", None, props=html_node_attr)
        html_node_parent = HTMLNode("p", "new html node", [html_node_child], props=html_node_attr)
        self.assertEqual(f'HTMLNode(p, new html node, [{repr(html_node_child)}], {html_node_attr})', repr(html_node_parent))

if __name__ == "__main__":
    unittest.main()
