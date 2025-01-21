# test connection

from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(_name_)

@app.route('/connect', methods=['POST'])
def connect_to_infura():
    # Print statement to log that a request has been received
    print("Received a POST request to /connect")

    try:
        data = request.get_json(force=True)  # Using force=True to ensure parsing even if the content-type header is not set properly
        print(f"Request data: {data}")  # Log the received data

        infura_project_id = data.get("infura_project_id")
        if not infura_project_id:
            print("Error: Infura Project ID is needed")  # Log error if no ID is provided
            return jsonify({"error": "Infura Project ID is needed"}), 400

        infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"
        web3 = Web3(Web3.HTTPProvider(infura_url))
        
        if web3.is_connected():
            print("Successfully connected to Infura")  # Log success message
            return jsonify({"message": "Successfully connected to Infura"}), 200
        else:
            print("Failed to connect to Infura")  # Log failure message
            return jsonify({"error": "Failed to connect to Infura"}), 500
    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Log unexpected errors
        return jsonify({"error": str(e)}), 500

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)  # Configure to run on all network interfaces for local testing
