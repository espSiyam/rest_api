from flask import Flask, request, jsonify
from utility.helpers import dummy_data, filter_data_query, scenario_response

app = Flask(__name__)

@app.route("/filter")
def filter_data():
    # Get query parameters from the request
    country = request.args.get("country")
    age = request.args.get("age")
    interest = request.args.get("interest")

    filter_data = filter_data_query(dummy_data, country, age, interest)

    if filter_data:
        return filter_data

@app.route('/response_code', methods=['GET'])
def api():
    scenario = request.args.get('scenario')

    response, status_code = scenario_response(scenario)

    return response, status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=000)
