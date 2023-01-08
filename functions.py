import requests
import json
# 662675887f17041bd4ed6406d2fb2ff8

ticker = "AAPL"
type = "balance-sheet"


def stockPull(ticker):
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{ticker}?apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url)
    return results.json()

def getfirstkey(results, index):
    keys = index
    key = index
    for keys in results:
        for key in keys:
            print(key)


def balancePull(ticker, period, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?Limit=[{years_of_data}&Period={period}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    balance_keys = ['cashAndCashEquivalents', 'shortTermInvestments', 'netReceivables', 'inventory', 
            'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet', 'otherNonCurrentAssets',
            'totalNonCurrentAssets', 'totalAssets', 'accountPayables', 'otherCurrentLiabilities', 'deferredRevenue',
            'longTermDebt', 'totalCurrentLiabilities', 'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities', 'totalLiabilities',
            'totalStockholdersEquity', 'totalLiabilitiesAndStockholdersEquity'] #
    balance_dict = {}
    
    for x in results:
        for key in x:
            if key in balance_keys:
                balance_dict[key] = results[0][key]
    return balance_dict
    

def cashflowPull(ticker, period, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?Limit=[{years_of_data}&Period={period}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    cashflow_keys= ['']
    return results[0]

print(cashflowPull(ticker, "annual", 1))

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
    results = requests.get(url).json()
    symbol = results[0]['symbol']
    name = results[0]['name']
    final = symbol + ': ' + name
    return final
    

def profilePull(ticker):
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    description = results[0]['description']
    return description

