import requests
import json
i=3
while i>0:
  line = input("Enter Stock Symbol: ")
  header = {'X-Finnhub-Token':'bvuvke748v6r5v92vlq0'} 
  r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={line}', headers = header)
  rjson = json.loads(r.content)
  value = rjson['c']
  previousClose = rjson['pc']
  percentChange = ((value - previousClose)/previousClose) * 100
  print(line + ':')
  print("\t Current Value", "$" + str(value), sep = " - ")
  print("\t Previous Close", "$" + str(previousClose), sep = " - ")
  print("\t Percent Change", "{:.3f}".format(percentChange)+"%", sep = " - ")
