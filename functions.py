import requests
import json
# 662675887f17041bd4ed6406d2fb2ff8

ticker = "AAPL"
period = 'annual'


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
    proper_keys = ['Cash and Cash Equivalents', 'Short Term Investments', 'Net Receivables', 'Inventory', 
            'Other Current Assets', 'Total Current Assets', 'Property Plant Equipment Net', 'Other Non-Current Assets', 
            'Total Non-Current Assets', 'Total Assets', 'Account Payables', 'Other Current Liabilities', 'Deferred Revenue',
            'Long Term Debt', 'Total Current Liabilities', 'Other Non-Current Liabilites', 'Total Non-Current Liabilites', 
            'Total Liabilites', "Total Stockholders' Equity", "Total Liabilities and Stockholders' Equity"]

    for entry in results:
        for key in entry:
            if key in balance_keys:
                balance_dict[key] = results[0][key]
    
    balance_dict = {proper_keys[balance_keys.index(key)]: value for key, value in balance_dict.items()}
    return balance_dict
    

def cashflowPull(ticker, period, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?Limit=[{years_of_data}&Period={period}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    cashflow_keys= ['netIncome', 'depreciationAndAmortization', 'stockBasedCompensation', 'deferredIncomeTax',
            'changeInWorkingCapital', 'accountsReceivables', 'inventory', 'otherWorkingCapital', 'accountsPayable',
            'otherNonCashItems', 'netCashProvidedByOperatingActivities', 'investmentsInPropertyPlantAndEquipment', 
            'acquisitionsNet', 'purchasesOfInvestments', 'otherInvestingActivites', 'netCashUsedForInvestingActivites',
            'debtRepayment', 'commonStockRepurchased', 'dividendsPaid', 'netCashUsedProvidedByFinancingActivities',
            'netChangeInCash', 'cashAtBeginningOfPeriod', 'cashAtEndOfPeriod', 'capitalExpenditure', 'operatingCashFlow', 
            'freeCashFlow']
    cashflow_dict = {}
    proper_keys = ['Net Income', 'Depreciation and Amortization', 'Stock-Based Compensation', 'Deferred Income Tax', 
            'Change in Working Capital', 'Accounts Receivables', 'Inventory', 'Other Working Capital', 'Accounts Payable', 
            'Other Non Cash Items', 'Net Cash Provided by Operating Activities', 'Investments in Property Plant and Equipment', 
            'Acquisitions Net', 'Purchases of Investments', 'OtherInvestingActivities', 'Net Cash Used for Investing Activities', 
            'Debt Repayment','Common Stock Repurchased', 'Dividends Paid', 'Net Cash Used Provided by Financing Activities', 
            'Net Change in Cash', 'Cash at Beginning of Period','Cash At End of Period', 'Capital Expenditure', 
            'Operating Cash Flow', 'Free Cash Flow']

    for x in results:
        for key in x:
            if key in cashflow_keys:
                cashflow_dict[key] = results[0][key]

    cashflow_dict = {proper_keys[cashflow_keys.index(key)]: value for key, value in cashflow_dict.items()}
    return cashflow_dict

def incomePull(ticker, period, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?Limit=[{years_of_data}&Period={period}&apikey=662675887f17041bd4ed6406d2fb2ff8"
    results = requests.get(url).json()
    income_keys = ['revenue', 'costOfRevenue', 'grossProfit', 'researchAndDevelopmentExpenses', 'operatingExpenses', 'costAndExpenses', 
            'interestIncome', 'interestExpense', 'operatingIncome', 'incomeBeforeTax', 'incomeTaxExpense', 'netIncome',
            'eps', 'epsdiluted']
    income_dict = {}
    proper_keys = []
    for entry in results:
        for key in entry:
            if key in income_keys:
                income_dict[key] = results[0][key]
    income_dict = {proper_keys[income_keys.index(key)]: value for key, value in income_dict.items()}
    return income_dict


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


def stockSearch(ticker):
    url = f"https://financialmodelingprep.com/api/v3/search-ticker?query={ticker}&limit=1&exchange=NASDAQ&apikey=662675887f17041bd4ed6406d2fb2ff8"
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

