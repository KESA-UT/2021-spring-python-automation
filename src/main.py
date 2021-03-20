import os
import requests
import json
from datetime import datetime, timedelta

end_point = os.environ['alpaca_end_point']
end_point_for_data = os.environ['alpaca_end_point_for_data']
api_key = os.environ['alpaca_api_key']
secret_key = os.environ['alpaca_secret_key']

def getAccountInformation():
    # return account information in dictionary
    # example dictionary structure might be something like
    url = "{}/v2/account".format(end_point)
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key
    }
    r = requests.get(url, headers=headers)
    res = json.loads(r.text)
    return res
    

def getStockInformation(stock):
    # get yesterday's date at 09:00 CST time
    yesterday = datetime.now() - timedelta(1)
    calendarDate = datetime.strftime(yesterday, '%Y-%m-%d')
    targetStart = '{}T14:00:01Z'.format(calendarDate) # 14:00 UTC is 09:00 CST
    targetEnd = '{}T14:10:00Z'.format(calendarDate)

    url = "{}/v2/stocks/{}/trades?start={}&end={}&limit=1".format(end_point_for_data, stock.upper(), targetStart, targetEnd)
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key
    }
    r = requests.get(url, headers=headers)
    res = json.loads(r.text)
    return res

def displayInformation(accountInfo, stockInfos):
    # display account information
    print("Account Information:")
    print("  Account Number: {}".format(accountInfo["account_number"]))
    print("  Cash Amt: {}".format(accountInfo["cash"]))
    print()

    # TODO: display stock information
    print("Stock Information:")
    for info in stockInfos:
        print("  {}:".format(info["symbol"]))
        print("    price: ${}".format(info["trades"][0]["p"]))
    


def main():
    accountInfo = getAccountInformation()
    stocks = ['googl', 'aapl', 'fb', 'msft', 'amzn']
    stockInfos = []
    for stock in stocks:
        stockInfo = getStockInformation(stock)
        stockInfos.append(stockInfo)
    displayInformation(accountInfo, stockInfos)

if __name__ == '__main__':
    main()