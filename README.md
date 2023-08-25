# Uniswap Transaction Analyzer

The Uniswap Transaction Analyzer is a Python-based utility that fetches the most recent swaps from Uniswap (using TheGraph's subgraph for Uniswap V3), filters them based on a minimum USD transaction value provided by the user, and then sorts the resulting addresses by their total transaction volume in USD. The tool also fetches the current ETH balance for each address using the Etherscan API.

## Features:

1. Fetch the most recent `n` swaps from Uniswap V3.
2. Filter swaps based on a user-specified minimum USD transaction value.
3. Aggregate and sort addresses based on their total transaction volume (in USD).
4. Fetch the current ETH balance of each address from Etherscan.
5. Export the aggregated and sorted data to a CSV file for further analysis.

## Prerequisites:

- Python 3.x
- Requests library (`pip install requests`)

## Usage:

1. Ensure you have Python 3.x installed.
2. Install the required libraries: `pip install requests`.
3. Run the script: `python main.py`.
4. Enter the number of recent swaps you'd like to fetch when prompted.
5. Provide a minimum USD transaction value to filter the results.
6. The script will then display the sorted addresses based on transaction volume and also export the data to a CSV file.

## Code Structure:

- `get_last_n_swaps(n)`: Fetches the last `n` swaps from Uniswap V3, returning the address (`origin`) and the transaction amount in USD (`amountUSD`).

- `get_eth_balance(address)`: Fetches the current ETH balance of a given address using the Etherscan API.

- `export_to_csv(sorted_wallets, filename="wallets.csv")`: Exports the aggregated data to a CSV file.

## Important Note:

Replace the placeholder `ETHERSCAN_API_KEY` in the script with your actual Etherscan API key for accurate and uninterrupted ETH balance fetching.
