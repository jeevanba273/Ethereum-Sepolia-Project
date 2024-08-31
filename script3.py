# # wallet balance check

# from web3 import Web3, HTTPProvider
# from requests.exceptions import RequestException
# import time

# # Replace with your Infura Project ID
# infura_project_id = "dde4a14c79c34a43b17ebc32f22ce6a4"

# # Infura endpoint for Sepolia
# infura_url = f"https://sepolia.infura.io/v3/dde4a14c79c34a43b17ebc32f22ce6a4"

# # Connect to Infura
# web3 = Web3(Web3.HTTPProvider(infura_url))

# # Check connection
# if web3.is_connected():
#     print(f"Successfully connected to Infura (Sepolia)")
# else:
#     raise Exception("Failed to connect to Infura")

# # Wallet address to monitor
# wallet_address = web3.to_checksum_address("0x5c41DB360Ff70A9EA4699769888E86acF3ef2a12".lower())

# # Function to get the current balance
# def get_balance(address):
#     balance_wei = web3.eth.get_balance(address)
#     balance_eth = web3.from_wei(balance_wei, 'ether')
#     return balance_eth

# # Print initial balance
# initial_balance = get_balance(wallet_address)
# print(f"balance: {initial_balance} ETH")





# from web3 import Web3
# import sys

# def main():
#     # Get Infura Project ID and wallet address from command line arguments
#     if len(sys.argv) != 3:
#         print("Error: Please provide both Infura Project ID and wallet address")
#         sys.exit(1)

#     infura_project_id = sys.argv[1]
#     wallet_address = sys.argv[2]

#     # Generate Infura URL
#     infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"

#     # Connect to Infura
#     web3 = Web3(Web3.HTTPProvider(infura_url))

#     # Check connection
#     if web3.is_connected():
#         print(f"Successfully connected to Infura (Sepolia)")
#     else:
#         print("Failed to connect to Infura")
#         sys.exit(1)

#     # Convert wallet address to checksum address
#     wallet_address = web3.to_checksum_address(wallet_address.lower())

#     # Function to get the current balance
#     def get_balance(address):
#         balance_wei = web3.eth.get_balance(address)
#         balance_eth = web3.from_wei(balance_wei, 'ether')
#         return balance_eth

#     # Print balance
#     balance = get_balance(wallet_address)
#     print(f"Balance: {balance} ETH")

# if __name__ == "__main__":
#     main()





# import sys
# from web3 import Web3

# def main():
#     if len(sys.argv) != 3:
#         print("Usage: script3.py <infura_project_id> <wallet_address>")
#         return

#     infura_project_id = sys.argv[1]
#     wallet_address = sys.argv[2]

#     infura_url = f"https://mainnet.infura.io/v3/{infura_project_id}"
#     web3 = Web3(Web3.HTTPProvider(infura_url))

#     if not web3.is_connected():
#         print("Failed to connect to Infura")
#         return

#     try:
#         balance = web3.eth.get_balance(wallet_address)
#         ether_balance = web3.from_wei(balance, 'ether')
#         print(f"Balance for the wallet is: {ether_balance} ETH")
#     except Exception as e:
#         print(f"Error fetching balance: {str(e)}")

# if __name__ == "__main__":
#     main()







import sys
from web3 import Web3

def check_balance(infura_project_id, wallet_address):
    try:
        web3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{infura_project_id}"))
        if not web3.is_connected():
            print("Error: Unable to connect to the Ethereum network.")
            return

        balance = web3.eth.get_balance(wallet_address)
        eth_balance = web3.from_wei(balance, 'ether')
        print(f"Balance of the wallet is : {eth_balance} ETH")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script3.py <infura_project_id> <wallet_address>")
    else:
        infura_project_id = sys.argv[1]
        wallet_address = sys.argv[2]
        check_balance(infura_project_id, wallet_address)
