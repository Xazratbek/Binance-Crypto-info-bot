import requests
import datetime as dt

def get_response(crypto_pair):
    time = dt.datetime.now()
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto_pair.upper()}"
    data = requests.get(key)
    data = data.json()
    if data['symbol']:
        return (f"Valyuta juftligi: {data['symbol']} 💸\n\nXozirgi narxi: {data['price']} 💲\n\nSo'rov yuborilgan vaqt: {time.hour}:{time.minute}:{time.second} ⌚️")
