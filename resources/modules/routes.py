from flask import Blueprint, jsonify, request

modules_blueprint = Blueprint('modules', __name__)

# Sample data
modules = {}

@modules_blueprint.route('/modules/', methods=['GET'])
def get_modules():
    return jsonify(modules)

@modules_blueprint.route('/modules/<module_name>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_module(module_name):
    if request.method == 'GET':
        return jsonify(modules.get(module_name, {}))
    elif request.method == 'POST':
        modules[module_name] = request.json
        return jsonify(modules[module_name])
    elif request.method == 'PUT':
        modules[module_name].update(request.json)
        return jsonify(modules[module_name])
    elif request.method == 'DELETE':
        del modules[module_name]
        return jsonify({'message': 'Module deleted successfully'})
