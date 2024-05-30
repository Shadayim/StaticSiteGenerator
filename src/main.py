from textnode import TextNode
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    text_node = TextNode("This is a text node","bold","https://www.boot.dev")
    

    html_node_child1 = HtmlNode("img", "first child", None, {"href": "https://www.google.com", "target": "_blank"})
    html_node_child2 = HtmlNode("img", "second child", None, {"href": "https://www.google.com", "target": "_blank"})  

    html_node = HtmlNode("a", "this is a link", [html_node_child1, html_node_child2], {"href": "https://www.google.com", "target": "_blank"})

    leaf = LeafNode("p", "leaf paragraph", {"href": "https://www.google.com", "target": "_blank"}) 

    parent_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])

    #result = parent_node.to_html()

    #print(text_node)
    #print(html_node)
    #print(leaf)

    print(parent_node.to_html())
    


if __name__ == '__main__':
    main()