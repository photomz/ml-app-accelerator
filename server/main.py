# Import necessary modules
from embeddings import embeddings
from flask import Flask, request, jsonify
from db import DBHandler

# Create a Flask application
app = Flask(__name__)
db = DBHandler()

# Enable CORS for all routes
@app.after_request
def add_cors_headers(response):
    # Set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Define a route for getting embeddings
@app.route('/analogy')
def get_analogy():
    # Get the values of query parameters A, B, and C from the request URL
    A = request.args.get('A')
    B = request.args.get('B')
    C = request.args.get('C')

    # Compute the analogy using the embeddings module
    Ds = embeddings.compute_analogy(A, B, C)

    # Retrieve the first result from the computed analogies if available, otherwise set D to None
    D = Ds[0] if len(Ds) else None

    # Log the request
    db.log_request(A, B, C, D)

    # Return the result as a JSON object
    return jsonify({'word': D})

@app.route('/logs')
def get_logs():
    # Retrieve all logs from the database
    logs = db.get_all_logs()

    # Return the logs as a JSON response
    return jsonify(logs)

# Define a route for health check
@app.route('/')
def health():
    # Return a JSON object indicating the status of the application
    return jsonify({'status': 'ok'})

# Run the Flask server if the script is executed directly
if __name__ == '__main__':
    # Start the Flask application on host 0.0.0.0 and port 3000
    # Special host 0.0.0.0 exposes our API endpoint to everyone on our WiFi network
    app.run(host='0.0.0.0', port=3000)