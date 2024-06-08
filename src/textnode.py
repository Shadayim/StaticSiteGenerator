from parentnode import ParentNode
from leafnode import LeafNode

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self):
        match self.text_type:
            case "text":
                return LeafNode(None,self.text, None).to_html()
            case "bold":
                return LeafNode("b",self.text, None).to_html()
            case "italic":
                return LeafNode("i",self.text, None).to_html()
            case "code":
                return LeafNode("code",self.text, None).to_html()
            case "link":
                return LeafNode("a",self.text, {'href': self.url}).to_html()
            case "image":
                return LeafNode("img", "", { 'src': self.url, 'alt': self.text }).to_html()
            case _:
                raise Exception("Invalid text type.")

    def __eq__(text_node, other_text_node) -> bool:
        if text_node.text == other_text_node.text and text_node.text_type == other_text_node.text_type and text_node.url == other_text_node.url:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


