from fastapi import FastAPI
from web3 import Web3
import requests

app = FastAPI()

@app.get("/connect/{infura_project_id}")
async def connect_to_infura(infura_project_id: str):
    try:
        web3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{infura_project_id}"))
        if web3.is_connected():
            return {"status": "success", "message": "Successfully connected to Infura."}
        else:
            return {"status": "failure", "message": "Failed to connect to Infura."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/check-ecommerce")
async def check_ecommerce_api():
    api_url = "https://springboot-ecommerce-project-lkfh.onrender.com/VITproject/connect"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return {"status": "success", "message": "Successfully connected to E-commerce API."}
        else:
            return {"status": "failure", "message": "Failed to connect to E-commerce API. Status code: " + str(response.status_code)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
