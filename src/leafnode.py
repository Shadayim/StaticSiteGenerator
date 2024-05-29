from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)
        if self.value is None:
            raise ValueError("LeafNode is missing required value")        

    def to_html(self):
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_Html()}>{self.value}</{self.tag}>"    
    
    def __repr__(self):
        props = self.props_to_Html()
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_Html()})"