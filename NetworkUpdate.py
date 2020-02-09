class NetworkUpdate:
    def __init__(self, node_list, link_list):
        self.nodes = []
        [self.nodes.extend([v]) for v in node_list.values()]
        self.links = []
        [self.links.extend([v]) for v in link_list.values()]
