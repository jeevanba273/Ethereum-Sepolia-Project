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

