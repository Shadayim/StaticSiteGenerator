from textnode import TextNode
from htmlnode import HtmlNode


def main():
    text_node = TextNode("This is a text node","bold","https://www.boot.dev")
    

    html_node_child1 = HtmlNode("<img>", "first child", None, {"href": "https://www.google.com", "target": "_blank"})
    html_node_child2 = HtmlNode("<img>", "second child", None, {"href": "https://www.google.com", "target": "_blank"})  

    html_node = HtmlNode("<a>", "this is a link", [html_node_child1, html_node_child2], {"href": "https://www.google.com", "target": "_blank"})

    print(text_node)
    print(html_node)


if __name__ == '__main__':
    main()