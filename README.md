# uniswap-v3-wallet-ranker

This Python tool retrieves the origin addresses of recent swaps from Uniswap V3 using TheGraph's API. It then fetches the current ETH balances of these addresses using the Etherscan API. The results are ranked in descending order based on balance, showcasing the richest wallets first. Additionally, users can specify a minimum balance threshold to filter and focus on wallets with significant balances.

## Prerequisites:

- Python 3
- `requests` library:
  ```bash
  pip install requests
  ```

## Configuration:

Before running the script, ensure to replace the `ETHERSCAN_API_KEY` in the script with your own API key obtained from Etherscan.

```python
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your Etherscan API Key
```

## How to Run:

1. Ensure you have the prerequisites installed and configured.
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter the number of swaps you wish to fetch when prompted.
4. Specify a minimum balance threshold when prompted.
5. Wait for the script to fetch and sort the addresses.
6. The script will display the Ethereum addresses and their corresponding balances in descending order. Optionally, results are saved to "wallets.csv" in the current directory.

## Key Functions:

1. **get_last_n_swaps(n)**
   - Fetches the origin addresses of the last `n` swaps from Uniswap V3 using TheGraph's API.
  
2. **get_eth_balance(address)**
   - Retrieves the ETH balance of a given Ethereum address using Etherscan's API.

## Features:
   - Fetch origin addresses from Uniswap V3 based on the last n swaps.
   - Retrieve ETH balances of these addresses.
   - Filter addresses based on a user-defined minimum balance threshold.
   - Display and optionally export results to a CSV file.

## Warning:

- Be cautious of Etherscan's rate limits; making too many rapid API calls can get your IP temporarily banned. If you're querying a large number of addresses in a short time, consider adding delays or using a premium API key to increase your rate limits.

## Disclaimer:

This tool is meant for informational purposes only. Always ensure you have the right permissions to fetch data from any platform or service.

## License:

This project is open-sourced under the MIT License. See the LICENSE file for more information. 
