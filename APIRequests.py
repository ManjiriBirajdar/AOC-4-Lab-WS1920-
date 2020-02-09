import Network
from NetworkUpdate import NetworkUpdate


def get_network():
    return NetworkUpdate(Network.nodes, Network.links)


def get_component(args):
    component_id = args.get('component_id')
    if component_id is None:
        return False, 'component_id is missing'
    component = Network.get_with_id(component_id)
    if component is None:
        return False, 'component not found'
    return True, component


def remove_component(form):
    component_id = form.get('component_id')
    if component_id is None:
        return False, 'component_id is missing'
    component = Network.get_with_id(component_id)
    if component is None:
        return False, 'component not found'
    Network.remove_with_id(component_id)
    return True, component_id


def modify_component(form):
    component_id = form.get('component_id')
    if component_id is None:
        return False, 'component_id is missing'
    component = Network.get_with_id(component_id)
    if component is None:
        return False, 'component not found'
    attributes = form.get('attributes')
    if attributes is None:
        return False, 'attributes is missing'
    component.attributes = attributes


def create_controller(form):
    ip = form.get('ip')
    port = form.get('port')
    name = form.get('name', default='controller')
    if ip is None:
        return False, 'ip is missing'
    if port is None:
        return False, 'port is missing'
    controller = Network.Controller(ip, port, name)
    return True, controller.add_to_network()


def create_host(form):
    ip = form.get('ip')
    mac = form.get('mac')
    name = form.get('name', default='host')
    if ip is None:
        return False, 'ip is missing'
    if mac is None:
        return False, 'mac is missing'
    host = Network.Host(ip, mac, name)
    return True, host.add_to_network()


def create_switch(form):
    ip = form.get('ip')
    host_count = form.get('host_count')
    name = form.get('name', default='switch')
    if ip is None:
        return False, 'ip is missing'
    if host_count is None:
        return False, 'host_count is missing'
    switch = Network.Switch(ip, host_count, name)
    return True, switch.add_to_network()


def create_link(form):
    source_id = form.get('source')
    target_id = form.get('target')
    source_port = form.get('source_port', default=80)
    target_port = form.get('target_port', default=80)
    if source_id is None:
        return False, 'source_id is missing'
    if target_id is None:
        return False, 'target_id is missing'
    source = Network.get_with_id(source_id)
    target = Network.get_with_id(target_id)
    if source is None:
        return False, 'source component not found'
    if target is None:
        return False, 'target component not found'
    link_type = get_link_type(source, target)
    link = Network.Link(source_id, target_id, source_port, target_port, link_type)
    return True, link.add_to_network()


def update_link(form):
    component_id = form.get('link_id')
    link_value = form.get('value')
    if component_id is None:
        return False, 'id is missing'
    if component_id is None:
        return False, 'value is missing'
    component = Network.get_with_id(component_id)
    if isinstance(component, Network.Link):
        component.link_value = link_value
        return True, component_id


def get_link_type(source, target):
    link_value = 0
    if isinstance(source, Network.Controller) and isinstance(target, Network.Controller):
        link_value = 40
    if isinstance(source, Network.Switch) and isinstance(target, Network.Switch):
        link_value = 20
    if isinstance(source, Network.Host) and isinstance(target, Network.Switch):
        link_value = 10
    if isinstance(source, Network.Switch) and isinstance(target, Network.Host):
        link_value = 10
    if isinstance(source, Network.Controller) and isinstance(target, Network.Switch):
        link_value = 30
    if isinstance(source, Network.Switch) and isinstance(target, Network.Controller):
        link_value = 30
    return link_value
