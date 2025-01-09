class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # If (arg) is None:
        # Tag -> Renders as raw text
        # Value -> Assumed to have children
        # Children -> Assumed to have a value
        # Props -> No attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            print("No props found! Returning empty string.")
            return ""
        # Make copy to ensure no accidental alterations
        test_props = self.props.copy()
        props_builder = list(map(lambda x: f' {x}="{test_props[x]}"', test_props))
        #print(" ".join(props_builder))
        return " ".join(props_builder)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value. No value was found.")
        if not self.tag:
            return self.value
        # Else we render a tag
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag.")
        if not self.children:
            raise ValueError("Missing children.")

        str_builder = ""
        for child in self.children:
            str_builder += child.to_html()

        return f"<{self.tag}>{str_builder}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

