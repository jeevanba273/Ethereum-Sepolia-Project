# 🚀 Ethereum - Sepolia Testnet Implementation

A web-based interface to interact with the **Ethereum Sepolia Testnet**, allowing users to perform various blockchain operations such as checking wallet balances, generating wallet addresses, sending transactions, and more.

🎯 **Live Project:**  
🔗 [Ethereum Sepolia Testnet Project](https://ethereum-sepolia-project-production.up.railway.app/)

---

## 🌟 Features

- ✅ **Check Connection** - Verify connection to the Ethereum Sepolia Testnet.
- 🔑 **Generate Wallet Address** - Create a new Ethereum wallet.
- 💰 **Check Wallet Balance** - Retrieve the balance of an Ethereum address.
- 📤 **Send Transaction** - Send ETH from one wallet to another.
- 🔍 **Latest Transaction** - Fetch details of the most recent transaction.
- 📜 **Transactions in Last 20 Blocks** - Track recent transactions on the testnet.
- 📡 **Live Track Wallet** - Monitor real-time updates of a wallet.
- 🖋 **Verify Transaction Signature** - Ensure transaction authenticity.

---

## 📌 Prerequisites

Before running the project locally, make sure you have:

1. **[Infura.io](https://infura.io/)** account (for API access).
2. **[Node.js](https://nodejs.org/)** installed.
   
---

## 🔑 Getting API Access from Infura

To connect to the **Ethereum Sepolia Testnet**, follow these steps:

1. **Sign up at [Infura.io](https://infura.io/).**
2. **Create a new project** and select **Ethereum** as the network.
3. **Copy the Project ID** (needed for API access).
4. **Replace your Project ID** in the configuration.

```js
const INFURA_PROJECT_ID = "your_project_id_here";
const INFURA_URL = `https://sepolia.infura.io/v3/${INFURA_PROJECT_ID}`;
```
---

## 🏗 **Tech Stack Used**

### 🖥 **Frontend (User Interface)**
- **HTML** → Structure of the web interface.
- **CSS** → Styling and layout.
- **JavaScript** → Handles client-side logic and interactions.
- **WebSockets (`ws`)** → Real-time communication between frontend and backend.

### 🛠 **Backend (Server)**
- **Node.js** → JavaScript runtime for backend logic.
- **Express.js** → Web framework to serve static files and handle API requests.
- **WebSockets (`ws`)** → Handles real-time communication between the client and server.
- **Child Processes (`exec`, `spawn`)** → Runs Python scripts from the Node.js backend.

### 🔗 **Blockchain Integration**
- **Infura API** → Connects to the Ethereum Sepolia Testnet.
- **Web3.js (Node.js)** → Interacts with the Ethereum blockchain.
- **Web3.py (Python)** → Used in Python scripts for blockchain interactions.

### 🐍 **Python (Blockchain Scripts)**
- **Python 3** → Runs scripts for blockchain operations.
- **Web3.py** → Ethereum Python library to interact with smart contracts and transactions.
- **sys (System Arguments)** → Passes parameters from the backend to the scripts.

### 🌍 **Deployment & Hosting**
- **Render.com** → Deployed the project online.
- **Procfile** → Configuration for hosting on Render.
