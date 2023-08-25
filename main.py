import requests
import csv


ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETHERSCAN_API_KEY = "ETHERSCAN_API_KEY" # Replace with your Etherscan API Key

def get_last_n_swaps(n):
    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
    query = """
    {
        swaps(first: %s, orderBy: timestamp, orderDirection: desc) {
            origin
            amount0
            amount1
        }
    }
    """ % n

    response = requests.post(url, json={"query": query})
    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    return [swap['origin'] for swap in data["data"]["swaps"]]

def get_eth_balance(address):
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(ETHERSCAN_API_URL, params=params)
    data = response.json()

    if data['status'] != "1":
        raise Exception(data["message"])

    # Convert wei to ether
    return int(data["result"]) / 1e18

def export_to_csv(sorted_wallets, filename="wallets.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["Address", "Balance (ETH)"])
        
        # Write each wallet's details
        for address, balance in sorted_wallets:
            writer.writerow([address, f"{balance:.2f}"])

if __name__ == "__main__":
    n = int(input("Enter the number of swaps to fetch: "))
    
    # Get the minimum balance from the user
    min_balance = float(input("Enter the minimum ETH balance to filter: "))
    
    origin_addresses = get_last_n_swaps(n)

    # Getting unique addresses
    unique_addresses = list(set(origin_addresses))

    # Fetch balances and filter based on min_balance
    balances = {}
    for address in unique_addresses:
        balance = get_eth_balance(address)
        if balance >= min_balance:  # Filtering wallets with balance greater than or equal to min_balance
            balances[address] = balance

    # Sort by balance, richest to poorest
    sorted_wallets = sorted(balances.items(), key=lambda x: x[1], reverse=True)

    # Print results
    for address, balance in sorted_wallets:
        print(f"Address: {address}, Balance: {balance:.2f} ETH")

    # Export to CSV
    export_to_csv(sorted_wallets)

