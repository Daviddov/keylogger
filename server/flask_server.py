from flask import Flask, request, jsonify
from flask_cors import CORS  # תמיכה ב-CORS

app = Flask(__name__)
CORS(app)  # מאפשר לכל המקורות לגשת ל-API

@app.route("/api", methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type, expected JSON"}), 415  # בדיקה האם התוכן JSON

        data = request.get_json()  # קריאת הנתונים מהבקשה
        print("Received data:", data)
        return jsonify({"message": "Data received", "data": data}), 200
    else:
        print("Connect via GET")
        return jsonify({"message": "Hello from server"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
