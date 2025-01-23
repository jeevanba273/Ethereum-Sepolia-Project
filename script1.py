from flask import Flask, request, jsonify
import requests
from web3 import Web3

app = Flask(__name__)

# Existing endpoint to connect to Sepolia Infura
@app.route('/connect', methods=['POST'])
def connect_to_infura():
    data = request.get_json(force=True)  # Using force=True to ensure parsing even if the content-type header is not set properly
    infura_project_id = data.get("infura_project_id")
    if not infura_project_id:
        return jsonify({"error": "Infura Project ID is needed"}), 400

    infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"
    web3 = Web3(Web3.HTTPProvider(infura_url))
    
    if web3.is_connected():
        return jsonify({"message": "Successfully connected to Infura"}), 200
    else:
        return jsonify({"error": "Failed to connect to Infura"}), 500

# New endpoint to check connection to the e-commerce API
@app.route('/check-ecommerce-connection', methods=['GET'])
def check_ecommerce_connection():
    api_url = "https://springboot-ecommerce-project-lkfh.onrender.com/VITproject/connect"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to connect to the e-commerce API", "status": response.status_code}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
