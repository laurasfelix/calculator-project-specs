'''
File Name: main.py
Dependencies: none
Purpose: Contains code that runs the operations
'''
# import statements (if any)
import finnhub
import sys
finnhub_client = finnhub.Client(
    api_key="chobfq1r01qmdnlqj6t0chobfq1r01qmdnlqj6tg")  # getting information from api through import and finnhub_client

# Write your code here


def calc(input):  # this calculates the alpha and returns it
    stock_info = finnhub_client.company_basic_financials(
        input, 'all')  # gets info from api based on user input
    if len(stock_info) == 0:
        print("Wow. Not here!")
        sys.exit()
    risk_free = (stock_info["series"]["annual"]["currentRatio"][-1]["v"] /
                 stock_info["series"]["annual"]["currentRatio"][0]["v"]) - 1  # calculates risk free return
    market_return = (stock_info["metric"]["52WeekHigh"]-stock_info["metric"]
                     ["52WeekLow"])/stock_info["metric"]["52WeekPriceReturnDaily"]  # calculate market return
    alpha = risk_free + \
        stock_info["metric"]["beta"] * \
        (market_return - risk_free)  # calculates alpha based on the above info, and gets beta from api
    return alpha  # returns it
