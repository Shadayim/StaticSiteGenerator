class HtmlNode:
    def __init__(self, tag = None, value= None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_Html(self):
        result = ""
        
        if self.props is None:
            return result

        for prop in self.props:
            result = result + f" {prop}=\"{self.props[prop]}\""
        
        return result
        
    def __repr__(self):

        props = self.props_to_Html()
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {props})"
    


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)
        if self.value is None:
            raise ValueError("LeafNode is missing required value")
        

    def to_html(self):
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_Html()}>{self.value}<\{self.tag}>"

