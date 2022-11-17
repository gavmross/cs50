import requests
import json
import sys

# print(response.json())
# print(json.dumps(response.json(), indent=2))


def query():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    information = response.json()
    price = information['bpi']["USD"]['rate_float']
    try:
     float(sys.argv[1])
    except (requests.RequestException, IndexError, ValueError):
        sys.exit()
    else:
        total = price * float(sys.argv[1])
        return "{:,}".format(total)

print(query())
