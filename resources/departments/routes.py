from flask import Blueprint, jsonify, request

departments_blueprint = Blueprint('departments', __name__)

# Sample data
departments = {}

@departments_blueprint.route('/faculties/<faculty_name>/departments/', methods=['GET'])
def get_departments(faculty_name):
    return jsonify(departments.get(faculty_name, {}))

@departments_blueprint.route('/faculties/<faculty_name>/departments/<department_name>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_department(faculty_name, department_name):
    if request.method == 'GET':
        return jsonify(departments.get(faculty_name, {}).get(department_name, {}))
    elif request.method == 'POST':
        departments[faculty_name][department_name] = request.json
        return jsonify(departments[faculty_name][department_name])
    elif request.method == 'PUT':
        departments[faculty_name][department_name].update(request.json)
        return jsonify(departments[faculty_name][department_name])
    elif request.method == 'DELETE':
        del departments[faculty_name][department_name]
        return jsonify({'message': 'Department deleted successfully'})
