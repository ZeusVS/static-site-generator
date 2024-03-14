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

