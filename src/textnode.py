class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(text_node, other_text_node) -> bool:
        if text_node.text == other_text_node.text and text_node.text_type == other_text_node.text_type and text_node.url == other_text_node.url:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


