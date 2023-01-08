import requests
import tabulate
import json
# 662675887f17041bd4ed6406d2fb2ff8


def stockPull(ticker):
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{ticker}?apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url)
    return results.json()

def getfirstkey(results, index):
    keys = index
    key = index
    for keys in results:
        for key in keys:
            print(key)


def balancePull(ticker, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?Limit=[{years_of_data}&Period=annual&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    balance_keys = ['cashAndCashEquivalents', 'shortTermInvestments', 'netReceivables', 'inventory', 
            'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet', 'otherNonCurrentAssets',
            'totalNonCurrentAssets', 'totalAssets', 'accountPayables', 'otherCurrentLiabilities', 'deferredRevenue',
            'longTermDebt', 'totalCurrentLiabilities', 'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities', 'totalLiabilities',
            'totalStockholdersEquity', 'totalLiabilitiesAndStockholdersEquity']
    balance_dict = {}
    proper_keys = ['Cash and Cash Equivalents', 'Short Term Investments', 'Net Receivables', 'Inventory', 
            'Other Current Assets', 'Total Current Assets', 'Property Plant Equipment Net', 'Other Non-Current Assets', 
            'Total Non-Current Assets', 'Total Assets', 'Account Payables', 'Other Current Liabilities', 'Deferred Revenue',
            'Long Term Debt', 'Total Current Liabilities', 'Other Non-Current Liabilites', 'Total Non-Current Liabilites', 
            'Total Liabilites', "Total Stockholders' Equity", "Total Liabilities and Stockholders' Equity"]
    
    for entry in results:
        for key in entry:
            if key in balance_keys:
                for count in range(years_of_data):
                    balance_dict[key] = results[count][key]
                count += 1

    balance_dict = {proper_keys[balance_keys.index(key)]: value for key, value in balance_dict.items()}
    return balance_dict

def balancePull_final(ticker, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?Limit=[{years_of_data}&Period=annual&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    date_sorted={}
    
    for i in list(range(years_of_data)):
        x = (balancePull(ticker, i+1))
        date_sorted[results[i]['date']] = x
        year = list(date_sorted.keys())        
        sections = list(date_sorted.values())[i]



        table = [year, sections]
        table = list(map(list, zip(*table)))

        #print(tabulate.tabulate(table, headers = ['YEAR', 'INFO']))
        print(sections)

print(balancePull_final('AAPL', 3))


def cashflowPull(ticker, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?Limit=[{years_of_data}&Period=annual&apikey=be7330815374d314431e8fd46431980f"
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
            'Acquisitions Net', 'Purchases of Investments', 'Other Investing Activities', 'Net Cash Used for Investing Activities', 
            'Debt Repayment','Common Stock Repurchased', 'Dividends Paid', 'Net Cash Used Provided by Financing Activities', 
            'Net Change in Cash', 'Cash at Beginning of Period','Cash At End of Period', 'Capital Expenditure', 
            'Operating Cash Flow', 'Free Cash Flow']

    for x in results:
        for key in x:
            if key in cashflow_keys:
                for count in range(years_of_data):
                    cashflow_dict[key] = results[count][key]
                count += 1

    cashflow_dict = {proper_keys[cashflow_keys.index(key)]: value for key, value in cashflow_dict.items()}
    return cashflow_dict

def cashflowPull_final(ticker, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?Limit=[{years_of_data}&Period=annual&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    date_sorted={}
    for i in list(range(years_of_data)):
       x = (cashflowPull(ticker, i+1))
       date_sorted[results[i]['date']] = x
    return date_sorted

def incomePull(ticker, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?Limit=[{years_of_data}&Period=annual&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    income_keys = ['revenue', 'costOfRevenue', 'grossProfit', 'researchAndDevelopmentExpenses', 'operatingExpenses', 'costAndExpenses', 
            'interestIncome', 'interestExpense', 'operatingIncome', 'incomeBeforeTax', 'incomeTaxExpense', 'netIncome',
            'eps', 'epsdiluted']
    income_dict = {}
    proper_keys = ['Revenue', 'Cost of Revenue', 'Gross Profit', 'Research and Development Expenses', 'Operating Expenses', 'Cost and Expenses',
    'Interest Income', 'Interest Expense', 'Operating Income', 'Income Before Tax', 'Income Tax Expense', 'Net Income', 'Eps', 'Epsdiluted']

    for entry in results:
        for key in entry:
            if key in income_keys:
                for count in range(years_of_data):
                    income_dict[key] = results[count][key]
    
    income_dict = {proper_keys[income_keys.index(key)]: value for key, value in income_dict.items()}
    return income_dict

def incomePull_final(ticker, years_of_data):
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?Limit=[{years_of_data}&Period=annual&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    date_sorted={}
    for i in list(range(years_of_data)):
       x = (incomePull(ticker, i+1))
       date_sorted[results[i]['date']] = x
    return date_sorted

'''
def growthPull(type, ticker):
    url = f"https://financialmodelingprep.com/api/v3/{type}-statement-growth/{ticker}?apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url)
    return results.json()
'''

def pricetargetPull(ticker):
    url = f"https://financialmodelingprep.com/api/v4/price-target?symbol={ticker}&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url)
    return results.json()


def historicemployeePull(ticker):
    url = f"https://financialmodelingprep.com/api/v4/historical/employee_count?symbol={ticker}&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    employeecount = results[0]['employeeCount']
    return employeecount


def stockSearch(ticker):
    url = f"https://financialmodelingprep.com/api/v3/search-ticker?query={ticker}&limit=1&exchange=NASDAQ&apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    symbol = results[0]['symbol']
    name = results[0]['name']
    final = symbol + ': ' + name
    return final
   

def profilePull(ticker):
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    description = results[0]['description']
    return description

def stockPrice(ticker):
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{ticker}?apikey=be7330815374d314431e8fd46431980f"
    results = requests.get(url).json()
    price = results[0]['price']
    return price