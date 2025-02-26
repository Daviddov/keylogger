import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type, expected JSON"}), 415
        data = request.get_json()
        print("Received data:", data)
        return jsonify({"message": "Data received", "data": data}), 200
    else:
        print("Connect via GET")
        return jsonify({"message": "Hello from server"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
