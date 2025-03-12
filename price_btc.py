import requests

def get_btc_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate_float']

def usd_to_satoshi(usd_amount, btc_price):
    satoshi_per_btc = 100_000_000
    return (usd_amount / btc_price) * satoshi_per_btc



if __name__ == "__main__":
    btc_price = get_btc_price()
    print("*********************************")
    print(f"Current Bitcoin price: ${btc_price:.2f}")
    satoshis = usd_to_satoshi(1, btc_price)
    print(f"1 USD is equivalent to {satoshis:.0f} satoshis")
    print("*********************************")

