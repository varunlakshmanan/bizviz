import requests
import pandas as pd
from src.ibm_api.stock_data import get_stock_data_yf
from src.data.fbp import get_list_of_prices,get_money, predict_price
import pickle
import datetime

# csv = requests.get('https://raw.githubusercontent.com/IBM/watson-stock-market-predictor/master/data/AAPL.csv')
# df = pd.read_csv('https://raw.githubusercontent.com/IBM/watson-stock-market-predictor/master/data/AAPL.csv', index_col=0)
#
# df.to_csv('AAPL.csv')


# time = 4
# money = 40
# dict = {}
# low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
# medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
# high_risk_stock_list = ['TSLA', 'AMZN', 'NVDA', 'AAPL']
# # get_stock_data_yf(low_risk_stock_list)
# list_of_prices = []
# for stock in low_risk_stock_list:
#     with open('../models/'+stock+'.pkl', 'rb') as f:
#         model = pickle.load(f)
#     list_of_projected = predict_price(stock, model, time)
#     list_of_prices.append(list_of_projected)
# low_risk = get_money(stock_list=low_risk_stock_list, list_of_prices=list_of_prices, money=money)
# dict['low_risk'] = low_risk
# list_of_prices = []
# for stock in medium_risk_stock_list:
#     with open('../models/' + stock + '.pkl', 'rb') as f:
#         model = pickle.load(f)
#     list_of_projected = predict_price(stock, model, time)
#     list_of_prices.append(list_of_projected)
# medium_risk = get_money(stock_list=medium_risk_stock_list, list_of_prices=list_of_prices, money=money)
# dict['medium_risk'] = medium_risk
# # get_stock_data_yf(medium_risk_stock_list)
# # list_of_prices = get_list_of_prices(medium_risk_stock_list, time)
# # medium_risk = get_money(stock_list=medium_risk_stock_list, list_of_prices=list_of_prices, money=money)
# # dict['medium_risk'] = medium_risk
# list_of_prices = []
# for stock in high_risk_stock_list:
#     with open('../models/' + stock + '.pkl', 'rb') as f:
#         model = pickle.load(f)
#     list_of_projected = predict_price(stock, model, time)
#     list_of_prices.append(list_of_projected)
# high_risk = get_money(stock_list=high_risk_stock_list, list_of_prices=list_of_prices, money=money)
# dict['high_risk'] = high_risk
# print(dict)

curr_string = "March 2017"
curr_string = "1 " + curr_string
print(curr_string)
d = datetime.datetime.strptime(curr_string, '%d %B %Y')
s = datetime.datetime.strftime(d, '%m-%d-%Y')
s += " GMT"
print(s)