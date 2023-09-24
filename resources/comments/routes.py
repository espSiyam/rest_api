from flask import Blueprint, jsonify, request

comments_blueprint = Blueprint('comments', __name__)

# Sample data
comments = {}

@comments_blueprint.route('/modules/<module_name>/courses/<course_name>/comments/', methods=['GET'])
def get_comments(module_name, course_name):
    return jsonify(comments.get(module_name, {}).get(course_name, {}))

@comments_blueprint.route('/modules/<module_name>/courses/<course_name>/comments/<comment_name>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_comment(module_name, course_name, comment_name):
    if request.method == 'GET':
        return jsonify(comments.get(module_name, {}).get(course_name, {}).get(comment_name, {}))
    elif request.method == 'POST':
        comments[module_name][course_name][comment_name] = request.json
        return jsonify(comments[module_name][course_name][comment_name])
    elif request.method == 'PUT':
        comments[module_name][course_name][comment_name].update(request.json)
        return jsonify(comments[module_name][course_name][comment_name])
    elif request.method == 'DELETE':
        del comments[module_name][course_name][comment_name]
        return jsonify({'message': 'Comment deleted successfully'})
