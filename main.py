from flask import Flask
from resources.modules.routes import modules_blueprint
from resources.courses.routes import courses_blueprint
from resources.comments.routes import comments_blueprint
from resources.faculties.routes import faculties_blueprint
from resources.departments.routes import departments_blueprint
from resources.staffs.routes import staffs_blueprint

app = Flask(__name__)

app.register_blueprint(modules_blueprint)
app.register_blueprint(courses_blueprint)
app.register_blueprint(comments_blueprint)
app.register_blueprint(faculties_blueprint)
app.register_blueprint(departments_blueprint)
app.register_blueprint(staffs_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
