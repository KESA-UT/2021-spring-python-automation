import os
import requests
import json
from datetime import datetime, timedelta

end_point = os.environ['alpaca_end_point'] # https://paper-api.alpaca.markets
end_point_for_data = os.environ['alpaca_end_point_for_data'] # https://data.alpaca.markets
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

def createJsonFile():
    # check if stocks.json exists
    # if not
    #   create a stocks.json file
    
    # TODO: create file if not exist


    # once the file is created above (if not already existed), parse the file and return a dict of all the information
    # if the file has been just created, it will return an empty dict {}
    return {}

def getStockInformationFromJson(jsonContent, stocks):
    # this is the wrapper function to initiate updating stock information
    # iterate (make a for loop) over stocks
    # for each stock, get the most recent information from jsonContent
    # if there's no stock information in jsonContent, that means we don't own any of that stock
    # in that case, buy
    # if any information is present, get the current price for stock, compare with the previous price saved in jsonContent
    # do the business logic from there accordingly
    for stock in stocks:
        # get information from jsonContent here
        stockPrice = None # change this with information fround from jsonContent
        updatedPrice = None # this will the be the current price of the stock
        numShare = 0

        if stockPrice is None:
            # we don't have any of this stock, please buy 5 shares (you can change the number of shares)
            # then update stockPrice
            buyStockAndReturnPrice(stock)
            numShare = 5 # we now own the stock
        else:
            # we have some of this stock, get the current price and compare it with previous price
            # then print what actions have been taken here
            stockInfo = getStockInformation(stock)
            # TODO: business logic
            # use buyStockAndReturnPrice and sellStockAndReturnPrice if needed

            numShare = 0 # update this variable with number of shares we own after actions have been taken

        # now that the price is updated, save that info to json file
        updateJson(stock, updatedPrice, numShare)

def buyStockAndReturnPrice(stock):
    # we don't have any of this stock, please buy 5 shares (you can change the number of shares)
    # then update stockPrice
    # print how much of which stock we bought at which price here
    # return how much share we bought
    return 5

def sellStockAndReturnPrice(stock):
    # For simplicity, sell all the shares we have
    # we could improve this logic to sell partial shares of what we own, but let's do it later
    # print how much of which stock we sold at which price here and what the gain is
    return 0

def updateJson(stock, updatedPrice, numShare):
    # complete this function to update json file
    # 2 things need to happen
    # if numShare is 0, then we don't own any of this stock, remove any information about them in json file
    # else update the information
    if numShare > 0:
        # we bought some of the stock, update the json file

    else:
        # we sold all the stock, delete any information about the stock from json file
        
    pass

def main():
    stocks = ['googl', 'aapl', 'fb', 'msft', 'amzn']
    accountInfo = getAccountInformation()
    jsonContent = createJsonFile()
    getStockInformationFromJson(jsonContent, stocks)

    # all the logs will be generated inside getSotkcInformationFromJson function for now
    # displayInformation(accountInfo, stockInfos)


if __name__ == '__main__':
    main()