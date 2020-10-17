import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def get_stock_data(stock_list):
    current_date = datetime.datetime.now()
    ten_year = current_date - relativedelta(years=10)
    current_date = current_date.strftime("%Y-%m-%d")
    ten_year = ten_year.strftime("%Y-%m-%d")

    df = pd.DataFrame()

    for stock in stock_list:
        stock_data = yf.download(stock, start=ten_year, end=current_date)
        print(stock_data)
        df = pd.concat((df, stock_data), axis=1)

    df.to_csv('../data/stock_data.csv')

stock_list = ['AAPL', 'AMZN', 'TSLA']
get_stock_data(stock_list)