from flask import Blueprint, jsonify, request

faculties_blueprint = Blueprint('faculties', __name__)

# Sample data
faculties = {}

@faculties_blueprint.route('/faculties/', methods=['GET'])
def get_faculties():
    return jsonify(faculties)

@faculties_blueprint.route('/faculties/<faculty_name>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_faculty(faculty_name):
    if request.method == 'GET':
        return jsonify(faculties.get(faculty_name, {}))
    elif request.method == 'POST':
        faculties[faculty_name] = request.json
        return jsonify(faculties[faculty_name])
    elif request.method == 'PUT':
        faculties[faculty_name].update(request.json)
        return jsonify(faculties[faculty_name])
    elif request.method == 'DELETE':
        del faculties[faculty_name]
        return jsonify({'message': 'Faculty deleted successfully'})
