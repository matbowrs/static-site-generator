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
            print("No props found!")
            return ""
        # Make copy to ensure no accidental alterations
        test_props = self.props.copy()
        props_builder = list(map(lambda x: f'"{x}"="{test_props[x]}"', test_props))
        print(" ".join(props_builder))
        return " ".join(props_builder)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"


