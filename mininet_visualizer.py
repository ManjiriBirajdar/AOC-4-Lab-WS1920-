import json

import jsonpickle
from flask import Flask, request

from APIRequests import *
from APIResponse import PostResponse, GetResponse, PutResponse, DeleteResponse

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Word!'


@app.route('/network', methods=['GET'])
def network():
    print_graph()
    return jsonpickle.encode(get_network(), unpicklable=False)


@app.route('/controller', methods=['GET', 'POST', 'DELETE'])
def controller():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_controller(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    print_graph()
    return jsonpickle.encode(response, unpicklable=False)


@app.route('/host', methods=['GET', 'POST', 'DELETE'])
def host():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_host(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    print_graph()
    return jsonpickle.encode(response, unpicklable=False)


@app.route('/switch', methods=['GET', 'POST', 'DELETE'])
def switch():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_switch(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    print_graph()
    return jsonpickle.encode(response, unpicklable=False)


@app.route('/link', methods=['GET', 'PUT', 'POST', 'DELETE'])
def link():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_link(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'PUT':
        success, data = update_link(request.form)
        response = PutResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    print_graph()
    return jsonpickle.encode(response, unpicklable=False)


def print_graph():
    network_graph = get_network()
    with open('graph.json', 'w') as outfile:
        json.dump(network_graph, outfile, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
