from flask import Flask, jsonify, request 
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#TARGET URL FOR THE ESP32 SERVER
ESP32_URL = "http://192.168.4.1"


@app.route('/', methods=['GET'])
def handle_root():

    return "Mock: Root Response", 200
    """
    Proxy the root GET request to the ESP32 server.
    """
    try:
        response = requests.get(f"{ESP32_URL}/")
        return response.content, response.status_code, response.headers.items()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/control-method', methods=['POST'])
def handle_control_method():

    # Mock response for control-method POST
    action = request.form.get('action', 'none')
    return f"Mock: Received action = {action}", 200
    """
    Proxy the POST request to the ESP32 server's /control-method endpoint.
    """
    try:
        # Extract POST data from the client
        action = request.form.get('action')
        if not action:
            return jsonify({"error": "Missing 'action' parameter"}), 400

        # Forward the request to the ESP32 server
        response = requests.post(f"{ESP32_URL}/control-method", data={"action": action})
        return response.content, response.status_code, response.headers.items()
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/check-wifi', methods=['GET'])
def check_wifi():
    # Mock response for check-wifi GET
    return "Mock: Wi-Fi Status = Connected", 200


if __name__ == '__main__':
    app.run(host='10.255.134.1', port=5001)

