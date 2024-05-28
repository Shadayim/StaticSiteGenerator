class HtmlNode:
    def __init__(self = None, tag = None, value= None, children = None, props = None):
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