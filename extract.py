import requests
import json
from datetime import datetime, timedelta

from requests.models import parse_header_links


# url ='https://api.exchangerate.host/latest'
# #url = 'https://api.exchangerate.host/convert?from=USD&to=CAD'
# response = requests.get(url)
# data = response.text
# parsed = json.loads(data)
# date = (parsed["date"])
# #datetime.today() - timedelta(days=10)
# print(date)
# print(parsed)

# cad_rate = parsed["info"]["rate"]
# print("On " + date + " CAD equals " + str(cad_rate) + " USD")


response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']

# with open("covid19.json", "w") as file: 
#     file.write(parse_json)

with open('covid19.json', 'w') as outfile:
    json.dump(parse_json, outfile)


# print("Active cases in South Andaman:", active_case)
# print(parse_json['Andaman and Nicobar Islands'])
#print(parse_json["Andaman and Nicobar Islands"])

 # def parse(self, response):  #mandatory
    #     with open("books.html", "wb") as file: #save to html file
    #         file.write(response.body)



# Read JSON file into dataframe
# df = spark.read.json("/Users/DOU2274/Desktop/LearningProjects/covid19.json")
# df.printSchema()
# df.show()

# # Read multiline json file
# multiline_df = spark.read.option("multiline","true") \
#       .json("/Users/DOU2274/Desktop/LearningProjects/covid19.json")
# multiline_df.show()  