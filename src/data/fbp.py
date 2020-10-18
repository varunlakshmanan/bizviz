from fbprophet import Prophet
import datetime
#from dateutil.easter import easter
import pandas as pd
from dateutil.relativedelta import relativedelta
#from yahoo_finance import Share
import yfinance as yf
import pickle
import stockquotes

def get_list_of_prices(stock_list, num_of_months):
    df = pd.read_csv('../data/stock_data.csv')
    count = 1
    list_of_prices = []
    for stock in stock_list:
        list_of_projected = {}
        stock_data = df.iloc[:, count:count+7]
        count+=7
        col_indices = [0,1]
        new_names = ['ds', 'y']
        old_names = stock_data.columns[col_indices]
        stock_data.rename(columns=dict(zip(old_names, new_names)), inplace=True)
        stock_data = stock_data.filter(items=['ds', 'y'])
        model = Prophet(daily_seasonality=False, weekly_seasonality=False, yearly_seasonality=True, changepoint_prior_scale=0.05, changepoints=None)
        model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
        model.fit(stock_data)

        pkl_path = "../models/"+stock+".pkl"
        with open(pkl_path, "wb") as f:
            # Pickle the 'Prophet' model using the highest protocol available.
            pickle.dump(model, f)

        #makes prediction one year in advance
        future_data = model.make_future_dataframe(periods=((num_of_months+1)*30))
        forecast = model.predict(future_data)
        forecasted_price = forecast[['ds', 'yhat']]
        today = datetime.datetime.now()
        for i in range(num_of_months):
            future = today + relativedelta(months=i + 1)
            future = future.strftime("%m-01-%Y")
            # future += "-01"
            value = forecasted_price[forecasted_price['ds'] == future].values[0][1]
            future += ' GMT'
            list_of_projected[future] = value
        list_of_prices.append(list_of_projected)
        #forecasted_price.to_csv('future_data.csv')
    return list_of_prices

def predict_price(stock, model, num_of_months):
    list_of_projected = {}
    future_data = model.make_future_dataframe(periods=((num_of_months + 1) * 30))
    forecast = model.predict(future_data)
    forecasted_price = forecast[['ds', 'yhat']]
    today = datetime.datetime.now()
    for i in range(num_of_months):
        future = today + relativedelta(months=i + 1)
        future = future.strftime("%m-01-%Y")
        # future += "-01"
        value = forecasted_price[forecasted_price['ds'] == future].values[0][1]
        future += ' GMT'
        list_of_projected[future] = value
    #list_of_prices.append(list_of_projected)
    # forecasted_price.to_csv('future_data.csv')
    return list_of_projected

def get_money(stock_list, list_of_prices, money):
    #divides money evenly among stocks
    stock_money = money / len(stock_list)
    dict = {}
    count = 0
    # today = datetime.datetime.now()
    # today = today.strftime("%Y-%m-%d")
    for stock in stock_list:
        # share = Share(stock)
        #stock_price = yf.download(stock, start=today, end=today)
        stock_obj = stockquotes.Stock(stock)
        stock_price = stock_obj.current_price
        # stock_price = stock_price['Open'].values[0]
        #print(stock_price)
        num_of_shares = stock_money / float(stock_price)
        list_of_stock = list_of_prices[count]
        #print(list_of_stock)
        # i = 1
        for date, price in list_of_stock.items():
            uprice = num_of_shares * price
            # s = str(i)
            if (date in dict.keys()):
                dict[date] = dict[date]+ uprice
            else:
                dict[date] = uprice
            #i+=1
        count+=1
    return dict

#num_of_months = 5
# low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
#medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
#high_risk_stock_list = ['TSLA', 'AMZN', 'NVDA', 'AAPL']
#list_of_prices = get_list_of_prices(high_risk_stock_list, num_of_months)
#print(list_of_prices)
#temp_list = [{'2020-11-01': 444.58105600107984, '2020-12-01': 476.3930626472659, '2021-01-01': 513.7873154199672, '2021-02-01': 551.9584350369109, '2021-03-01': 576.6159015623272}, {'2020-11-01': 3314.3813289361915, '2020-12-01': 3403.458750136123, '2021-01-01': 3471.237244499922, '2021-02-01': 3643.584211818914, '2021-03-01': 3689.151627413864}, {'2020-11-01': 549.3280722258825, '2020-12-01': 562.9468660336015, '2021-01-01': 587.3330001816589, '2021-02-01': 609.6957059514913, '2021-03-01': 621.3325014357209}, {'2020-11-01': 123.39610206550843, '2020-12-01': 124.17790857381368, '2021-01-01': 127.15492871073009, '2021-02-01': 131.13093697525866, '2021-03-01': 131.60752995602556}]
#money = get_money(high_risk_stock_list, list_of_prices, 50)
#print(money)