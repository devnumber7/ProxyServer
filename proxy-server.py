from flask import Flask, jsonify, request
import requests
import logging

app = Flask(__name__)

# Mapping of device IDs to their respective ESP32 URLs
DEVICE_URLS = {
    "1": "http://192.168.4.12",  # ESP32 URL for the first device
    "2": "http://192.168.4.10",  # ESP32 URL for the second device
    # Add more devices as needed
}

@app.route('/control-method', methods=['POST'])
def handle_control_method():
    try:
        # Log incoming request data for debugging
        logging.info(f"Received request: {request.form}")

        # Extract action and device_id parameters from the client request
        action = request.form.get('action')
        device_id = request.form.get('device_id')

        if not action:
            return jsonify({"error": "ion as e:
        logging.error(f"Error communicating with ESP32 device: {e}")
        return jsonify({"error": "Failed to communicate with ESP32 device"}), 502
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Run the Flask app with SSL context
    app.run(host="198.82.190.97", port=5000, ssl_context=('cert.pem', 'key.pem'))Missing 'action' parameter"}), 400
        if not device_id:
            return jsonify({"error": "Missing 'device_id' parameter"}), 400

        # Get the ESP32 URL for the given device_id
        esp_url = DEVICE_URLS.get(device_id)
        if not esp_url:
            return jsonify({"error": f"No ESP32 URL found for device_id '{device_id}'"}), 404

        # Forward the request to the ESP32 server
        response = requests.post(
            f"{esp_url}/control-method",
            data={"action": action},
            timeout=5  # Optional: set a timeout for the request
        )

        # Return the response from the ESP32 server
        return response.content, response.status_code, response.headers.items()
    except requests.exceptions.RequestExcept
