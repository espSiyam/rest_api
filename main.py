from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route to handle the root URL ("/") and return "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # Run the Flask app on localhost (127.0.0.1) and port 5000
    app.run(host="0.0.0.0", port=5000)