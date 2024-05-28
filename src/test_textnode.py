import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is another textnode", "bold", "https://boot.dev")

        self.assertNotEqual(node, node2)

    def test_not_equal_text_type(self):
        node = TextNode("This is a text node", "italic", "https://boot.dev")
        node2 = TextNode("This is a textnode", "bold", "https://boot.dev")

        self.assertNotEqual(node, node2)

    def test_not_equal_text_url(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a textnode", "bold", "https://not.boot.dev")

        self.assertNotEqual(node, node2)

    def test_equal_when_url_is_None(self):
        node = TextNode("This is a text node", "bold", None)

        self.assertRaises(TypeError)


if __name__ == "__main__":
    unittest.main()
