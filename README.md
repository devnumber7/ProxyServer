# Flask-based Proxy Server 

This project is a Flask-based proxy server that acts as a bridge between a client and multiple ESP32 devices. It enables clients to control ESP32 devices using HTTP requests by forwarding requests to the appropriate ESP32 servers. The project supports the smarthub project for the SMART team under IDPro@VT

## Features

- Maps multiple ESP32 devices to their unique IDs for easy control
- Accepts client requests with `action` and `device_id` parameters
- Forwards requests to the appropriate ESP32 device
- Handles communication errors gracefully with appropriate HTTP responses
- Securely serves the application over HTTPS

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-esp32-controller.git
   cd flask-esp32-controller
   ```

2. Install dependencies:
   ```bash
   pip install flask requests
   ```

3. Generate SSL certificates (`cert.pem` and `key.pem`) for HTTPS:
   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
   ```

4. Update the `DEVICE_URLS` dictionary in the script with your ESP32 device URLs.

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Send a POST request to the `/control-method` endpoint with the following parameters:
   - `action`: The desired action to perform on the ESP32 device
   - `device_id`: The ID of the device to control

   Example request:
   ```bash
   curl -X POST -F "action=turn_on" -F "device_id=1" https://198.82.190.97:5000/control-method --insecure
   ```

3. The server will forward the request to the specified ESP32 device and return the device's response.

## Endpoints

### POST /control-method

Handles requests to control ESP32 devices.

#### Parameters

- `action` (required): Action to perform
- `device_id` (required): ID of the target ESP32 device

#### Responses

- `200`: Success, response from the ESP32 device
- `400`: Missing parameters
- `404`: Device ID not found
- `502`: Failed communication with the ESP32 device
- `500`: Internal server error

## Logging

Logs are written to the console and include details of incoming requests and errors.
