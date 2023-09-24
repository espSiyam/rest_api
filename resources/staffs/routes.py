from flask import Blueprint, jsonify, request

staffs_blueprint = Blueprint('staffs', __name__)

# Sample data
staffs = {}

@staffs_blueprint.route('/faculties/<faculty_name>/departments/<department_name>/staffs/', methods=['GET'])
def get_staffs(faculty_name, department_name):
    return jsonify(staffs.get(faculty_name, {}).get(department_name, {}))

@staffs_blueprint.route('/faculties/<faculty_name>/departments/<department_name>/staffs/<staff_name>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_staff(faculty_name, department_name, staff_name):
    if request.method == 'GET':
        return jsonify(staffs.get(faculty_name, {}).get(department_name, {}).get(staff_name, {}))
    elif request.method == 'POST':
        staffs[faculty_name][department_name][staff_name] = request.json
        return jsonify(staffs[faculty_name][department_name][staff_name])
    elif request.method == 'PUT':
        staffs[faculty_name][department_name][staff_name].update(request.json)
        return jsonify(staffs[faculty_name][department_name][staff_name])
    elif request.method == 'DELETE':
        del staffs[faculty_name][department_name][staff_name]
        return jsonify({'message': 'Staff deleted successfully'})
