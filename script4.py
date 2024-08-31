# # send a transaction

# from web3 import Web3

# # Connect to Infura
# infura_url = "https://sepolia.infura.io/v3/dde4a14c79c34a43b17ebc32f22ce6a4"
# web3 = Web3(Web3.HTTPProvider(infura_url))

# # Check connection
# if web3.is_connected():
#     print("Successfully connected to Infura")
# else:
#     raise Exception("Failed to connect to Infura")

# # Your account address and private key
# sender_address = "0x5c41DB360Ff70A9EA4699769888E86acF3ef2a12"
# private_key = "0xcd74f42123bbe15ec1ddd2e5fbf5b26a5e7e3d39fc7627b67d924cba3103e17f"

# # Recipient address
# recipient_address = "0x9686F0468BC994B1993Ac2FBa949a51256D3E09d"

# # Transaction details
# value_to_send = web3.to_wei(0.01, 'ether')
# gas_limit = 21000  # Standard gas limit for ETH transfer
# gas_price = web3.to_wei('50', 'gwei')
# chain_id = 11155111  # Sepolia chain ID

# # Get sender's balance
# balance = web3.eth.get_balance(sender_address)
# total_tx_cost = value_to_send + (gas_limit * gas_price)

# print(f"Sender balance: {web3.from_wei(balance, 'ether')} ETH")
# print(f"Total transaction cost: {web3.from_wei(total_tx_cost, 'ether')} ETH")

# # Check if the balance is sufficient
# if balance < total_tx_cost:
#     print(f"Insufficient funds\nBalance: {web3.from_wei(balance, 'ether')} ETH, Required Balance: {web3.from_wei(total_tx_cost, 'ether')} ETH")
# else:
#     nonce = web3.eth.get_transaction_count(sender_address)
#     tx = {
#         'nonce': nonce,
#         'to': recipient_address,
#         'value': value_to_send,
#         'gas': gas_limit,
#         'gasPrice': gas_price,
#         'chainId': chain_id
#     }

#     # Sign the transaction
#     signed_tx = web3.eth.account.sign_transaction(tx, private_key)

#     # Send the transaction
#     try:
#         tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#         print(f"Transaction hash: {web3.to_hex(tx_hash)}")
        
#         # Wait for the transaction receipt
#         tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
#         # Check if the transaction was successful
#         if tx_receipt.status == 1:
#             print("Transaction was successful!")
#             print(f"Transaction inserted into block number: {tx_receipt.blockNumber}")
#             updated_balance = web3.eth.get_balance(sender_address)
#             print(f"Updated sender balance: {web3.from_wei(updated_balance, 'ether')} ETH")
#         else:
#             print("Transaction failed!")
#     except ValueError as e:
#         print(f"Transaction failed: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")




import sys
from web3 import Web3

# Get user inputs from command-line arguments
infura_project_id = sys.argv[1]
sender_address = sys.argv[2]
private_key = sys.argv[3]
recipient_address = sys.argv[4]

infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"

# Connect to Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if web3.is_connected():
    print("Successfully connected to Infura")
else:
    raise Exception("Failed to connect to Infura")

# Transaction details
value_to_send = web3.to_wei(0.01, 'ether')
gas_limit = 21000  # Standard gas limit for ETH transfer
gas_price = web3.to_wei('50', 'gwei')
chain_id = 11155111  # Sepolia chain ID

# Get sender's balance
balance = web3.eth.get_balance(sender_address)
total_tx_cost = value_to_send + (gas_limit * gas_price)

print(f"Sender balance: {web3.from_wei(balance, 'ether')} ETH")
print(f"Total transaction cost: {web3.from_wei(total_tx_cost, 'ether')} ETH")

# Check if the balance is sufficient
if balance < total_tx_cost:
    print(f"Insufficient funds\nBalance: {web3.from_wei(balance, 'ether')} ETH, Required Balance: {web3.from_wei(total_tx_cost, 'ether')} ETH")
else:
    nonce = web3.eth.get_transaction_count(sender_address)
    tx = {
        'nonce': nonce,
        'to': recipient_address,
        'value': value_to_send,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'chainId': chain_id
    }

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)

    # Send the transaction
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction hash: {web3.to_hex(tx_hash)}")
        
        # Wait for the transaction receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        # Check if the transaction was successful
        if tx_receipt.status == 1:
            print("Transaction was successful!")
            print(f"Transaction inserted into block number: {tx_receipt.blockNumber}")
            updated_balance = web3.eth.get_balance(sender_address)
            print(f"Updated sender balance: {web3.from_wei(updated_balance, 'ether')} ETH")
        else:
            print("Transaction failed!")
    except ValueError as e:
        print(f"Transaction failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")