import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("hello")
        self.assertEqual(node.props_to_html(), "")

    def test_eq(self):
        node = HTMLNode(props = {"hello": "one"})
        result = " hello=\"one\""
        self.assertEqual(node.props_to_html(), result)

    def test_eq_two(self):
        node = HTMLNode(props = {"key": "one", "hello": "two"})
        result = " key=\"one\" hello=\"two\""
        self.assertEqual(node.props_to_html(), result)

    def test_repr(self):
        node = HTMLNode(props = {'key': 'one', 'hello': 'two'})
        result = "tag: None, value: None, children: None, props: {'key': 'one', 'hello': 'two'}"
        self.assertEqual(str(node), result)

if __name__ == "__main__":
    unittest.main()
