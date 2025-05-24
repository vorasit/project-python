import requests
import json

def get_btc_in_usd():
    """Fetches the current price of Bitcoin in USD from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        # Safely access nested dictionary keys for price
        price = data.get("bitcoin", {}).get("usd")
        if price is None:
            # Handle cases where the expected data structure is not found
            print("Error: Could not find Bitcoin price in USD in the API response.")
            return None
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from CoinGecko API.")
        return None

def get_usd_to_thb_rate():
    """Fetches the current USD to THB exchange rate from ExchangeRate-API."""
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        # Safely access nested dictionary keys for rate
        rate = data.get("rates", {}).get("THB")
        if rate is None:
            # Handle cases where the expected data structure is not found
            print("Error: Could not find THB exchange rate in the API response.")
            return None
        return rate
    except requests.exceptions.RequestException as e:
        print(f"Error fetching USD to THB exchange rate: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from ExchangeRate-API.")
        return None

if __name__ == "__main__":
    # Fetch Bitcoin price in USD
    btc_usd = get_btc_in_usd()
    # Fetch USD to THB exchange rate
    usd_thb_rate = get_usd_to_thb_rate()

    # Proceed only if both API calls were successful
    if btc_usd is not None and usd_thb_rate is not None:
        # Calculate Bitcoin price in THB
        btc_thb = btc_usd * usd_thb_rate
        # Print the results formatted to two decimal places
        print(f"Bitcoin Price: ${btc_usd:,.2f} USD")
        print(f"USD to THB Exchange Rate: {usd_thb_rate:,.2f} THB")
        print(f"Bitcoin Price: {btc_thb:,.2f} THB")
    else:
        # Print specific error messages if API calls failed
        if btc_usd is None:
            print("Failed to fetch Bitcoin price in USD.")
        if usd_thb_rate is None:
            print("Failed to fetch USD to THB exchange rate.")
