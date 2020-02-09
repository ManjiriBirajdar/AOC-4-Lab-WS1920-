nodes = {}
links = {}
id_count = 0
updated = False


def get_id():
    global id_count
    id_count = id_count + 1
    return str(id_count)


def get_with_id(component_id):
    if component_id in nodes:
        return nodes[component_id]
    if component_id in links:
        return links[component_id]


def remove_with_id(component_id):
    if component_id in nodes:
        nodes.pop(component_id)
    if component_id in links:
        links.pop(component_id)


class Component:
    def __init__(self, attributes):
        self.attributes = attributes


class Node(Component):
    def __init__(self, ip, name, attributes):
        super().__init__(attributes)
        self.ip = ip
        self.name = name

    def add_to_network(self):
        node_id = get_id()
        nodes[node_id] = self
        return node_id


class Controller(Node):
    def __init__(self, ip, port, name, attributes={}):
        super().__init__(ip, name, attributes)
        self.port = port


class Host(Node):
    def __init__(self, ip, mac, name, attributes={}):
        super().__init__(ip, name, attributes)
        self.mac = mac


class Switch(Node):
    def __init__(self, ip, host_count, name, attributes={}):
        super().__init__(ip, name, attributes)
        self.host_count = host_count


class Link(Component):
    def __init__(self, source_id, target_id, source_port, target_port, link_value, attributes={}):
        super().__init__(attributes)
        self.source_id = source_id
        self.target_id = target_id
        self.source_port = source_port
        self.target_port = target_port
        self.link_value = link_value
        self.messages = []

    def add_to_network(self):
        edge_id = get_id()
        links[edge_id] = self
        return edge_id

