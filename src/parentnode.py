from htmlnode import HtmlNode
from leafnode import LeafNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)    

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode is missing required tag")
        
        if self.children is None:
            raise ValueError("ParentNode is missing required children")        

        result = ""  
                           
        for child in self.children:                  
            result += child.to_html()
            

        return f"<{self.tag}{self.props_to_Html()}>{result}</{self.tag}>"
    
    def __repr__(self):        
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
