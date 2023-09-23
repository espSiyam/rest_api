from flask import Blueprint, jsonify, url_for, request
from app import db, Teacher, Faculty

hateoas = Blueprint('hateoas', __name__)


@hateoas.route('/teacher/<int:id>', methods=['GET'])
def get_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    teacher_data = {
        "id": teacher.id,
        "name": teacher.name,
        "surname": teacher.surname,
        "faculty_id": teacher.faculty_id,
        "links": [
            {"self": url_for("hateoas_api.get_teacher", id=id, _external=True)},
            {"faculty": url_for("hateoas_api.get_faculty", id=teacher.faculty_id, _external=True)}
        ]
    }
    return jsonify(teacher_data), 200


@hateoas.route('/faculty/<int:id>', methods=['GET'])
def get_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    teachers = faculty.teachers
    links = [{"self": url_for("hateoas.get_faculty", id=id, _external=True)}]

    for teacher in teachers:
        links.append({"teacher": url_for("hateoas.get_teacher", id=teacher.id, _external=True)})

    faculty_data = {
        "id": faculty.id,
        "name": faculty.name,
        "links": links
    }
    return jsonify(faculty_data), 200

@hateoas.route('/faculty', methods=['POST'])
def create_faculty():
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    new_faculty = Faculty(name=data["name"])
    db.session.add(new_faculty)
    db.session.commit()

    faculty_data = {
        "id": new_faculty.id,
        "name": new_faculty.name,
        "links": [{
            "self": url_for("hateoas.get_faculty", id=new_faculty.id, _external=True),
        }]
    }

    return jsonify(faculty_data), 201


@hateoas.route('/faculty/<int:faculty_id>/add_teacher', methods=['POST'])
def add_teacher_to_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    data = request.get_json()
    if "name" not in data or "surname" not in data:
        return jsonify({"error": "Missing 'name' or 'surname' fields"}), 400

    new_teacher = Teacher(name=data["name"], surname=data["surname"], faculty_id=faculty_id)
    db.session.add(new_teacher)
    faculty.teachers.append(new_teacher)
    db.session.flush()
    db.session.commit()

    teacher_data = {
        "id": new_teacher.id,
        "name": new_teacher.name,
        "surname": new_teacher.surname,
        "faculty_id": new_teacher.faculty_id,
        "links": [
            {"self": url_for("hateoas.get_teacher", id=new_teacher.id, _external=True)},
            {"faculty": url_for("hateoas.get_faculty", id=faculty_id, _external=True)}]
    }

    return jsonify(teacher_data), 201


@hateoas.route('/delete_all_test', methods=['POST'])
def clear_database_test():
    db.session.query(Teacher).delete()
    db.session.query(Faculty).delete()
    db.session.commit()
    return {"result": "good"}, 200
