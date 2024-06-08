import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode("This is a text node", "bold", "https://shadayim.eu")
        node2 = TextNode("This is a text node", "bold", "https://shadayim.eu")
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is a text node", "bold", "https://shadayim.eu")
        node2 = TextNode("This is another textnode", "bold", "https://shadayim.eu")

        self.assertNotEqual(node, node2)

    def test_not_equal_text_type(self):
        node = TextNode("This is a text node", "italic", "https://shadayim.eu")
        node2 = TextNode("This is a textnode", "bold", "https://shadayim.eu")

        self.assertNotEqual(node, node2)

    def test_not_equal_text_url(self):
        node = TextNode("This is a text node", "bold", "https://shadayim.eu")
        node2 = TextNode("This is a textnode", "bold", "https://not.shadayim.eu")

        self.assertNotEqual(node, node2)

    def test_to_html_invalid(self):
        with self.assertRaises(Exception):
            node = TextNode("Invalid type text node", "invalidtype", "https://shadayim.eu")
            node.text_node_to_html_node()

    def test_to_to_html_plain(self):
        node = TextNode("This is a plain text node", "text", "https://shadayim.eu")
        self.assertEqual(node.text_node_to_html_node(), "This is a plain text node")

    def test_to_to_html_bold(self):
        node = TextNode("This is a bold text node", "bold", "https://shadayim.eu")
        self.assertEqual(node.text_node_to_html_node(), "<b>This is a bold text node</b>")

    def test_to_to_html_italic(self):
        node = TextNode("This is an italic text node", "italic", "https://shadayim.eu")
        self.assertEqual(node.text_node_to_html_node(), "<i>This is an italic text node</i>")

    def test_to_to_html_code(self):
        node = TextNode("This is a code node", "code", "https://shadayim.eu")
        self.assertEqual(node.text_node_to_html_node(), "<code>This is a code node</code>")

    def test_to_to_html_link(self):
        node = TextNode("This is a link node", "link", "https://shadayim.eu")
        self.assertEqual(node.text_node_to_html_node(), "<a href=\"https://shadayim.eu\">This is a link node</a>")

    def test_to_to_html_image(self):
        node = TextNode("This is an img node", "image", "https://shadayim.eu")
        self.assertEqual(node.text_node_to_html_node(), "<img src=\"https://shadayim.eu\" alt=\"This is an img node\"></img>") 

if __name__ == "__main__":
    unittest.main()
