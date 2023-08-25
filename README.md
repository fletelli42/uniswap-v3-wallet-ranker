# uniswap-v3-wallet-ranker

This script retrieves and sorts Ethereum wallet addresses based on their ETH balances. It fetches the origin addresses from the last `n` swaps on Uniswap V3 and then fetches the current balances of these addresses using the Etherscan API. The results are then sorted in descending order based on the ETH balance, showing the richest wallet first.

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
4. Wait for the script to fetch and sort the addresses.
5. The script will display the Ethereum addresses and their corresponding balances in descending order.

## Key Functions:

1. **get_last_n_swaps(n)**
   - Fetches the origin addresses of the last `n` swaps from Uniswap V3 using TheGraph's API.
  
2. **get_eth_balance(address)**
   - Retrieves the ETH balance of a given Ethereum address using Etherscan's API.

## Warning:

- Be cautious of Etherscan's rate limits; making too many rapid API calls can get your IP temporarily banned. If you're querying a large number of addresses in a short time, consider adding delays or using a premium API key to increase your rate limits.

## Disclaimer:

This tool is meant for informational purposes only. Always ensure you have the right permissions to fetch data from any platform or service.

## License:

This project is open-sourced under the MIT License. See the LICENSE file for more information. 
