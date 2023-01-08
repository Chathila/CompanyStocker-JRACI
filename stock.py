import requests
import json


ticker = input('Enter ticker: ')
frm, to = map(str, input('Date Range: ').split())

def cryptoPull(ticker, frm, to):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/crypto/{ticker}?from={frm}&to={to}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()

print(cryptoPull(ticker, frm, to))