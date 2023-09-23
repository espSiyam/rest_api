from flask import Flask, request, jsonify
from utility.data import dummy_data
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return '<Teacher {} {}>'.format(self.name, self.surname)


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    teachers = db.relationship('Teacher', backref='Faculty', lazy=True)

    def __repr__(self):
        return '<Faculty {}>'.format(self.name)

#see hateoas_api.py
from hateoas_api import hateoas
app.register_blueprint(hateoas)


@app.route("/filter")
def filter_data():
    # Get query parameters from the request
    country = request.args.get("country")
    age = request.args.get("age")
    interest = request.args.get("interest")

    # Start with all data
    filtered_data = dummy_data

    # Filter by country
    if country:
        filtered_data = [item for item in filtered_data if item["country"].lower() == country.lower()]

    # Filter by age
    if age:
        try:
            age = int(age)
            filtered_data = [item for item in filtered_data if item["age"] == age]
        except ValueError:
            return jsonify({"error": "Invalid age parameter. Please provide an integer."}), 400

    # Filter by interest
    if interest:
        filtered_data = [item for item in filtered_data if item["interest"].lower() == interest.lower()]

    # Return the filtered data as JSON
    return jsonify(filtered_data)


@app.route('/response_code', methods=['GET'])
def api():
    scenario = request.args.get('scenario')

    if scenario == 'success':
        response = {
            'message': 'Request was successful!',
            'status_code': 200
        }
        status_code = 200
    elif scenario == 'bad_request':
        response = {
            'error': 'Bad Request',
            'message': 'The request is missing required data.',
            'status_code': 400
        }
        status_code = 400
    elif scenario == 'not_found':
        response = {
            'error': 'Not Found',
            'message': 'The requested resource does not exist.',
            'status_code': 404
        }
        status_code = 404
    elif scenario == 'server_error':
        response = {
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred on the server.',
            'status_code': 500
        }
        status_code = 500
    else:
        response = {
            'error': 'Invalid Scenario',
            'message': 'The specified scenario is not valid.',
            'status_code': 400
        }
        status_code = 400

    return jsonify(response), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



