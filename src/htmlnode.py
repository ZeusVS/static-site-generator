class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props= props

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

    def to_html(self):
        raise NotImplementedError("method not implemented")

    def props_to_html(self):
        if not self.props:
            return ""
        propsText = ""
        for prop in self.props:
            propsText += f" {prop}=\"{self.props[prop]}\""
        return propsText

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('Invalid HTML: no value')
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('Invalid parent HTML: no tag')
        if not self.children:
            raise ValueError('Invalid parent HTML: no children')
        htmlText = f"<{self.tag}>"
        for node in self.children:
            htmlText += node.to_html()
        htmlText += f"</{self.tag}>"
        return htmlText
