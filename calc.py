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

# this calculates the alpha and returns it


def calc(input):
    # gets info from api based on user input
    stock_info = finnhub_client.company_basic_financials(
        input, 'all')
    # If the input stock doesn't exist within the API
    if len(stock_info) == 0:
        print("Stock not found.")
        return 404

      # calculates risk free return:
      # (Last day of evaluation / First day of Evaluation) - 1
    risk_free = (stock_info["series"]["annual"]["currentRatio"][-1]["v"] /
                 stock_info["series"]["annual"]["currentRatio"][0]["v"]) - 1
    # Market Return:
    # Profits - Losses (basically average return)
    market_return = (stock_info["metric"]["52WeekHigh"]-stock_info["metric"]
                     ["52WeekLow"])/stock_info["metric"]["52WeekPriceReturnDaily"]
    # Alpha
    alpha = risk_free + \
        stock_info["metric"]["beta"] * \
        (market_return - risk_free)  # calculates alpha based on the above info, and gets beta from api
    return alpha  # returns it
