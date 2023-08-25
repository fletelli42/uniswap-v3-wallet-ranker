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
            amountUSD
        }
    }
    """ % n

    response = requests.post(url, json={"query": query})
    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    # Return the swaps with origin and amountUSD
    return [{'origin': swap['origin'], 'amountUSD': float(swap['amountUSD'])} for swap in data["data"]["swaps"]]


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
        writer.writerow(["Address", "Balance (ETH)", "Total Transaction Amount (USD)"])
        
        # Write each wallet's details
        for data in sorted_wallets:
            address, balance, amount_usd = data
            writer.writerow([address, f"{balance:.2f}", f"{amount_usd:.2f}"])


if __name__ == "__main__":
    n = int(input("Enter the number of swaps to fetch: "))
    
    swaps = get_last_n_swaps(n)
    
    min_usd_value = float(input("Enter the minimum USD transaction value to filter: "))
    filtered_swaps = [swap for swap in swaps if swap['amountUSD'] >= min_usd_value]
    
    # Getting unique addresses
    unique_addresses = list(set(swap['origin'] for swap in filtered_swaps))

    # Fetch balances
    balances = {}
    for address in unique_addresses:
        balance = get_eth_balance(address)
        balances[address] = balance

    # Aggregating transaction volume (amountUSD) for each address
    transaction_volumes = {}
    for swap in swaps:
        address = swap['origin']
        amount_usd = swap['amountUSD']
        
        if address not in transaction_volumes:
            transaction_volumes[address] = 0
        transaction_volumes[address] += amount_usd

    # Combine balances with their respective transaction volumes
    combined_data = []
    for address in unique_addresses:
        balance = get_eth_balance(address)
        combined_data.append((address, balance, transaction_volumes.get(address, 0)))

    # Sort by transaction volume, highest to lowest
    sorted_wallets = sorted(combined_data, key=lambda x: x[2], reverse=True)

    # Print results
    for address, balance, amount_usd in sorted_wallets:
        print(f"Address: {address}, Balance: {balance:.2f} ETH, Transaction Amount: ${amount_usd:.2f}")

    # Export to CSV
    export_to_csv(sorted_wallets)


