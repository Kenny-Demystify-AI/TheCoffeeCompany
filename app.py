from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")

    # Process or modify the data here if needed
    processed_data = {"processed": True, "original_data": data}

    # Example: Send data to another Azure service endpoint
    azure_endpoint = "https://example.azurewebsites.net/api/endpoint"
    response = requests.post(azure_endpoint, json=processed_data)

    # Return the response from the Azure endpoint to the client
    return jsonify({"azure_response": response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
