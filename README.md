# Bitcoin Price Converter

This script fetches the current price of Bitcoin in USD and converts it to Thai Baht (THB) using live exchange rates.
It first states that 1 Bitcoin equals 100,000,000 Satoshis. It then displays the price for this amount (1 BTC) in both USD and THB, along with the current USD to THB exchange rate.
Additionally, the script calculates and displays how many Satoshis can be obtained for 1 USD and for 1 THB based on the current rates.

## Dependencies

The script requires the `requests` Python library.

## Installation

Install the necessary library using pip:
```bash
pip install requests
```

## How to Run

Run the script from your terminal using:
```bash
python btc_price_converter.py
```
Alternatively, if you have `python3` aliased or are in an environment where `python` refers to Python 2, you might need to use:
```bash
python3 btc_price_converter.py
```

## Example Output

```
1 Bitcoin = 100,000,000 Satoshis
Price of 100,000,000 Satoshis (1 BTC): $65,000.00 USD
Current USD to THB Exchange Rate: 36.50 THB
Price of 100,000,000 Satoshis (1 BTC): 2,372,500.00 THB

For 1 USD, you can get 1,538 Satoshis.
For 1 THB, you can get 42 Satoshis.
```
*(Note: The prices, rates, and Satoshi amounts shown above are illustrative and will vary based on real-time data.)*

## Data Sources

This script uses the following APIs:
*   **CoinGecko**: For fetching the current price of Bitcoin in USD.
*   **ExchangeRate-API**: For fetching the current USD to THB exchange rate.

This script uses ExchangeRate-API for currency conversion. Please attribute them if you use this data: <a href="https://www.exchangerate-api.com">Rates By Exchange Rate API</a>.
