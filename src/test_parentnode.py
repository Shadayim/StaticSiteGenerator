import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text")                
            ],
        )
        self.assertRaises(ValueError)

    def test_no_children(self):
        node = ParentNode(
            "p",
            [],
        )
        self.assertRaises(ValueError)

    def test_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_grand_children(self):
        node = ParentNode("div", [ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],)]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>",
        )
if __name__ == "__main__":
    unittest.main()
    
