import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("hello")
        self.assertEqual(node.props_to_html(), "")

    def test_eq(self):
        node = HTMLNode(props = {"key": "one", "hello": "two"})
        result = " key=\"one\" hello=\"two\""
        self.assertEqual(node.props_to_html(), result)

    def test_repr(self):
        node = HTMLNode(props = {'key': 'one', 'hello': 'two'})
        result = "tag: None, value: None, children: None, props: {'key': 'one', 'hello': 'two'}"
        self.assertEqual(str(node), result)

    def test_leafnode(self):
        node = LeafNode(None, "This is raw text.")
        result = "This is raw text."
        self.assertEqual(node.to_html(), result)

    def test_leafnode_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), result)

    def test_leafnode_ref(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), result)

    def test_parentnode(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), result)

    def test_parentnode_multilevel(self):
        parent = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    ],
                )

        grandparent = ParentNode(
                "p",
                [
                    parent,
                    parent,
                    ],
                )
        result = "<p><p><b>Bold text</b>Normal text</p><p><b>Bold text</b>Normal text</p></p>"
        self.assertEqual(grandparent.to_html(), result)

if __name__ == "__main__":
    unittest.main()
