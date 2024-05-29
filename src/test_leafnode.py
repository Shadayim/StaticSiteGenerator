import unittest

from htmlnode import HtmlNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_throw_on_none_value(self):        
        with self.assertRaises(ValueError):
            node = LeafNode("div", None, {"href": "https://www.google.com", "target": "_blank"})

    def test_to_hmtl(self):        
        leaf = LeafNode("p", "leaf paragraph", {"href": "https://www.google.com", "target": "_blank"})        
        self.assertEqual(leaf.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">leaf paragraph</p>")

    def test_to_html_none_tag(self):
        leaf = LeafNode(None, "leaf paragraph", {"href": "https://www.google.com", "target": "_blank"}) 
        self.assertEqual(leaf.to_html(), "leaf paragraph")

if __name__ == "__main__":
    unittest.main()