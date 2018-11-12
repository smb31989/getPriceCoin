import configparser
import urllib.request
import json
import datetime
import time

urlCoin = ''

# Read in config file
Config = configparser.ConfigParser()
Config.read('config.config')

try:
    cointar = Config.get('coinSymbol','coin')
except:
    print("Error read config file")


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()
response = opener.open('https://api.coinmarketcap.com/v2/listings/')
rawData = json.load(response)
rawData2 = rawData['data']

#print(rawData2[1])

#ค้นหา id จาก coin symblo เช่น BTC จะให้ค่า id = 1
for i in range(0, len(rawData2)):

    #เข้าถึงตัวแปร list
    coinMember = rawData2[i]
    coinSym = coinMember['symbol']
    if coinSym == cointar:
        #print(coinMember['id'])

        #ได้ url ใหม่รวมกับ id ของ coin
        urlCoin = 'https://api.coinmarketcap.com/v2/ticker/' + str(coinMember['id']) + '/?convert=THB'
        #print(urlCoin)


#อ่านค่าราคา THB จาก URL ใหม่ที่รวม id coin แล้ว
response = opener.open(urlCoin)
rawData = json.load(response)

rawData2 = rawData['data']
rawData3 = rawData2['quotes']
rawData4 = rawData3['THB']
priceCoinTHB = rawData4['price']
print(priceCoinTHB)
    
