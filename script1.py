# test connection

import sys
from web3 import Web3

def main():
    if len(sys.argv) != 2:
        print("Usage: python script1.py <infura_url>")
        sys.exit(1)
    
    infura_project_id = sys.argv[1]
    infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"
    web3 = Web3(Web3.HTTPProvider(infura_url))
    
    if web3.is_connected():
        print("Successfully connected to Infura (Sepolia)\n")
    else:
        print("\nFailed to connect to Infura (Sepolia)\n")

if __name__ == "__main__":
    main()
