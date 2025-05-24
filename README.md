# Bitcoin Price Converter

This script fetches the current price of Bitcoin in USD and converts it to Thai Baht (THB) using live exchange rates.

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

## Data Sources

This script uses the following APIs:
*   **CoinGecko**: For fetching the current price of Bitcoin in USD.
*   **ExchangeRate-API**: For fetching the current USD to THB exchange rate.

This script uses ExchangeRate-API for currency conversion. Please attribute them if you use this data: <a href="https://www.exchangerate-api.com">Rates By Exchange Rate API</a>.
