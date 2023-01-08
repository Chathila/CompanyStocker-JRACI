import requests

APIKey = "662675887f17041bd4ed6406d2fb2ff8"

#specify company and years of data that we want
company_name = input("Please enter the company symbol: ")
years_of_data = input("Please enter how many years of data you want: ")

#using API
balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company_name}?Limit=[{years_of_data}&apikey={APIKey}")

#getting the json 
data = balance_sheet.json()

#getting specific data (testing)
total_current_assets = data[0]['totalCurrentAssets']
calendar_year = data[0]['calendarYear']
currency = data[0]['reportedCurrency']

print(f"TOTAL CURRENT ASSETS: {company_name} \nTotal current assets for {calendar_year}: ${total_current_assets} {currency}")