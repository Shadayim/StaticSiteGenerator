import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def props_to_hmtl(self):
        node = HtmlNode("p", "child paragraph", None, {"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_Html(), "href=\"https://www.google.com\" target=\"_blank\"")

    def test_none_props_to_hmtl(self):
        
        child = HtmlNode("p", "child paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        node = HtmlNode("div", None, [child], None)

        self.assertEqual(node.props_to_Html(), "")

if __name__ == "__main__":
    unittest.main()