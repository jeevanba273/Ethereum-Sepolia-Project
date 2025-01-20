#Test connection with Infura

from web3 import Web3
from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/connect', methods=['POST'])
def connectToInfura():
    HttpStatus_ok = 200
    HttpStatus_internalServerError = 500
    HttpStatus_badRequest = 400

    data = request.get_json()
    infuraProjectId = data.get("infura_project_id")
    if not infuraProjectId:
        return jsonify({"error": "Infura Project ID is needed"}), HttpStatus_badRequest

    # Corrected variable name
    infuraUrl = f"https://sepolia.infura.io/v3/{infuraProjectId}"
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    
    if web3.is_connected():
        return jsonify({"message": "Successfully connected to Infura"}), HttpStatus_ok
    else:
        return jsonify({"error": "Failed to connect to Infura (Sepolia)"}), HttpStatus_internalServerError


if __name__ == "__main__":
    app.run(host="13.228.225.19", port=8080) #include public ip address and port
