from flask import Blueprint, jsonify, request

courses_blueprint = Blueprint('courses', __name__)

# Sample data
courses = {}

@courses_blueprint.route('/modules/<module_name>/courses/', methods=['GET'])
def get_courses(module_name):
    return jsonify(courses.get(module_name, {}))

@courses_blueprint.route('/modules/<module_name>/courses/<course_name>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_course(module_name, course_name):
    if request.method == 'GET':
        return jsonify(courses.get(module_name, {}).get(course_name, {}))
    elif request.method == 'POST':
        courses[module_name][course_name] = request.json
        return jsonify(courses[module_name][course_name])
    elif request.method == 'PUT':
        courses[module_name][course_name].update(request.json)
        return jsonify(courses[module_name][course_name])
    elif request.method == 'DELETE':
        del courses[module_name][course_name]
        return jsonify({'message': 'Course deleted successfully'})
