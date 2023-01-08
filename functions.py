import requests
import json
# 662675887f17041bd4ed6406d2fb2ff8

ticker = "AAPL"
type = "annual"


def stockPull(ticker):
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{ticker}?apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()


def statementPull(type, ticker, period, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/{type}-statement/{ticker}?Limit=[{years_of_data}&Period={period}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()

def growthPull(type, ticker):
    url = f"https://financialmodelingprep.com/api/v3/{type}-statement-growth/{ticker}?apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()


def pricetargetPull(ticker):
    url = f"https://financialmodelingprep.com/api/v4/price-target?symbol={ticker}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()


def historicemployeePull(ticker):
    url = f"https://financialmodelingprep.com/api/v4/historical/employee_count?symbol={ticker}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    employeecount = results[0]['employeeCount']
    return employeecount


def stockSearch(ticker, limit, exchange):
    url = f"https://financialmodelingprep.com/api/v3/search-ticker?query={ticker}&limit={limit}&exchange={exchange}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()
    

def profilePull(ticker):
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    description = results[0]['description']
    return description

print(profilePull(ticker))