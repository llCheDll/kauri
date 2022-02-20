import requests

BASE_URL = 'https://api.binance.com/{}'
URI = 'api/v3/exchangeInfo?symbol=BTCUSDT'


def json_parser(url):
    request = requests.get(url)
    data = request.json()

    return data


if __name__ == '__main__':
    print(json_parser(BASE_URL.format(URI)))
