#In this tutorial, you will learn how to use Python to extract data from ExchangeRatesAPI.io 

#Reading and Parsing the API Output with Python
import requests #to connect to the URL
import json #to parse the JSON output and extract the data you need.

# Connect to the URL as if you are opening it in browser – figuratively 😉

# url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"
# response = requests.get(url)
# print(response)


# #Read the output:

# data = response.text
# #print(data)

# # Parse JSON – convert the string to JSON:

# parsed = json.loads(data)  #Note: Be careful, it is “loads” not “load”

# #print(json.dumps(parsed, indent=4))


# import requests
# import json
 
# url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"
 
# response = requests.get(url)
# data = response.text
# parsed = json.loads(data)
# date = parsed["date"]
 
# gbp_rate = parsed["rates"]["GBP"]
# usd_rate = parsed["rates"]["USD"]
# print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
# print("On " + date + " EUR equals " + str(usd_rate) + " USD")
 

# rencies to iterate them like this:

# Python
# bases = ["USD", "EUR", "GBP"]

# for base in bases:
#     url = "https://api.exchangeratesapi.io/latest?base=" + base

#     response = requests.get(url)
#     data = response.text
#     parsed = json.loads(data)

#     rates = parsed["rates"]

#     print("--------------- Rates in", base, "---------------")
#     for currency, rate in rates.items():
#         print(base, "=", currency, rate)


# #Changing API URL Parameters
# bases = ["USD", "EUR", "GBP"]
 
# for base in bases:
#     url = "https://api.exchangeratesapi.io/latest?base=" + base
 
#     response = requests.get(url)
#     data = response.text
#     parsed = json.loads(data)
 
#     rates = parsed["rates"]
 
#     print("--------------- Rates in", base, "---------------")
#     for currency, rate in rates.items():
#         print(base, "=", currency, rate)

#     #Simple Currency Converter
 
# base = input("Convert from: ")
# to = input("Convert to: ")
# amount = float(input("Amount: "))
 
# url = "https://api.exchangeratesapi.io/latest?base=" + base
 
# response = requests.get(url) 
# data = response.text 
# parsed = json.loads(data) 
# rates = parsed["rates"]
 
 
# for currency, rate in rates.items():
#     if currency == to:
#         conversion = rate * amount
#         print("1", base, "=", currency, rate)
#         print(amount, base, "=", currency, conversion)

#API with Access Key
#1- Go to fixer.io – as you can see, it defines itself as a “Foreign exchange
#rates and currency conversion JSON API”.

#2- Click “sign up free”, then select the free plan to the left by clicking the grey button “Get Free API Key“, and fill in the form to sign up.

#3- Now, on Fixer dashboard, you can see a label called “Your API Access Key” followed by a combination of numbers and strings which is the Access Key you need for your API URL to work.

#4- If you move to the “3-Step Quickstart Guide”, you can see all the URLs you can use which consists of several parts:
 
 #Acces Key
 #aa30619ec445b8fdb2b2bcb69125addf
#  http://data.fixer.io/api/latest?access_key=aa30619ec445b8fdb2b2bcb69125addf
#  If you want to determine the currency symbols, you can add another parameter after an ampersand mark “&” so the URL will be:

#http://data.fixer.io/api/latest?access_key=9d1f065a6a9816f9dd7667b0c9b26bab&symbols=USD,GBP

 
url = "http://data.fixer.io/api/latest?access_key=aa30619ec445b8fdb2b2bcb69125addf&symbols=USD,GBP"
 
response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]
 
gbp_rate = parsed["rates"]["GBP"]
usd_rate = parsed["rates"]["USD"]
print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(usd_rate) + " USD")