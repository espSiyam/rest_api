from flask import jsonify

dummy_data = [
    {"name": "John", "country": "USA", "age": 30, "interest": "programming"},
    {"name": "Alice", "country": "Canada", "age": 25, "interest": "music"},
    {"name": "Bob", "country": "UK", "age": 35, "interest": "sports"},
    {"name": "Eva", "country": "USA", "age": 28, "interest": "travel"},
]

def filter_data_query(filtered_data, country, age, interest):

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

def scenario_response(scenario):
    if scenario == 'success':
        response = {
            'message': 'Request was successful!',
        }
        status_code = 200

    elif scenario == 'bad_request':
        response = {
            'error': 'Bad Request',
            'message': 'The request is missing required data.',
        }
        status_code = 400

    elif scenario == 'not_found':
        response = {
            'error': 'Not Found',
            'message': 'The requested resource does not exist.',
        }
        status_code = 404

    elif scenario == 'server_error':
        response = {
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred on the server.',
        }
        status_code = 500

    else:
        response = {
            'error': 'Invalid Scenario',
            'message': 'The specified scenario is not valid.',
        }
        status_code = 400

    return jsonify(response), status_code