import requests

APIKey = "662675887f17041bd4ed6406d2fb2ff8"

#specify company and years of data that we want
company_name = input("Please enter the company symbol: ")
years_of_data = input("Please enter how many years of data you want: ")

#using API
balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company_name}?Limit=[{years_of_data}&apikey={APIKey}")

#getting the json 
print(balance_sheet.json())

