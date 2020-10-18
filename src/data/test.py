import requests
import pandas as pd
from src.ibm_api.stock_data import get_stock_data_yf
from src.data.fbp import get_list_of_prices,get_money

# csv = requests.get('https://raw.githubusercontent.com/IBM/watson-stock-market-predictor/master/data/AAPL.csv')
# df = pd.read_csv('https://raw.githubusercontent.com/IBM/watson-stock-market-predictor/master/data/AAPL.csv', index_col=0)
#
# df.to_csv('AAPL.csv')


time = 10
money = 40
list = []
low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
high_risk_stock_list = ['TSLA', 'AMZN', 'NVDA', 'AAPL']
get_stock_data_yf(low_risk_stock_list)
list_of_prices = get_list_of_prices(low_risk_stock_list, time)
low_risk = get_money(stock_list=low_risk_stock_list, list_of_prices=list_of_prices, money=money)
list.append(low_risk)
get_stock_data_yf(medium_risk_stock_list)
list_of_prices = get_list_of_prices(medium_risk_stock_list, time)
medium_risk = get_money(stock_list=medium_risk_stock_list, list_of_prices=list_of_prices, money=money)
list.append(medium_risk)
get_stock_data_yf(high_risk_stock_list)
list_of_prices = get_list_of_prices(high_risk_stock_list, time)
high_risk = get_money(stock_list=high_risk_stock_list, list_of_prices=list_of_prices, money=money)
list.append(high_risk)
print(list)