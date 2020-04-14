import requests
import csv

#get data from JSON

code = 'BBY'
main_api = ('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' +
            code + '&apikey=NRTEXH9M4O8KBA0R')
url  = main_api + urllib.parse.urlencode({'NYSE': code})

json_data = requests.get(url).json()

data = []

for key,value in json_data['Time Series (Daily)'].items():
    date = key
    sopen = value["1. open"]
    high = value["2. high"]
    low = value["3. low"]
    close = value["4. close"]
    volume = value["5. volume"]
    data.append(date)        
    data.append(sopen) 
    data.append(high) 
    data.append(low) 
    data.append(close)
    data.append(volume)
#divide list of data into groups of five each containing the values above
def divide_chunks(n): 
    for i in range(0, len(data), n):  
        yield data[i:i + n] 
  
chunks = list(divide_chunks(6))
chunks.pop(-1)

with open('C:\\python_work\\BBY-stockdata.csv', mode='w') as stockdata:
    stockdatacsv = csv.writer(stockdata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    i = 0
    while i <= len(chunks):
        try:
            print(chunks[i])
            i+= 1
            stockdatacsv.writerow(chunks[i])
        except IndexError:
            print("Done!")
            break
            stockdata.close()



