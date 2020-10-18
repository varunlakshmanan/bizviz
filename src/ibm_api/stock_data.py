import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import os


def get_stock_data_yf(stock_list):
    current_date = datetime.datetime.now()
    ten_year = current_date - relativedelta(years=4)
    current_date = current_date.strftime("%Y-%m-%d")
    ten_year = ten_year.strftime("%Y-%m-%d")

    df = pd.DataFrame()

    for stock in stock_list:
        stock_data = yf.download(stock, start=ten_year, end=current_date)
        stock_data.reset_index(inplace=True)
        print(stock_data)
        df = pd.concat((df, stock_data), axis=1)
    df.to_csv('../data/stock_data.csv')

# low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
#medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
# high_risk_stock_list = ['TSLA', 'AMZN', 'NVDA', 'AAPL']
#get_stock_data_yf(medium_risk_stock_list)