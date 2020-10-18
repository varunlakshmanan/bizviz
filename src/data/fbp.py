from fbprophet import Prophet
import datetime
#from dateutil.easter import easter
import pandas as pd
from dateutil.relativedelta import relativedelta
#from yahoo_finance import Share
import yfinance as yf
import pickle

def get_list_of_prices(stock_list, num_of_months):
    df = pd.read_csv('../data/stock_data.csv')
    count = 1
    list_of_prices = []
    for stock in stock_list:
        list_of_projected = []
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
            future = future.strftime("%Y-%m-%d")
            list_of_projected.append(forecasted_price[forecasted_price['ds']==future].values[0][1])
        list_of_prices.append(list_of_projected)
        #forecasted_price.to_csv('future_data.csv')
    return list_of_prices

def predict_price(stock, model, num_of_months):
    list_of_projected = []
    future_data = model.make_future_dataframe(periods=((num_of_months + 1) * 30))
    forecast = model.predict(future_data)
    forecasted_price = forecast[['ds', 'yhat']]
    today = datetime.datetime.now()
    for i in range(num_of_months):
        future = today + relativedelta(months=i + 1)
        future = future.strftime("%Y-%m-%d")
        list_of_projected.append(forecasted_price[forecasted_price['ds'] == future].values[0][1])
    #list_of_prices.append(list_of_projected)
    # forecasted_price.to_csv('future_data.csv')
    return list_of_projected

def get_money(stock_list, list_of_prices, money):
    #divides money evenly among stocks
    stock_money = money / len(stock_list)
    dict = {}
    count = 0
    today = datetime.datetime.now()
    today = today.strftime("%Y-%m-%d")
    for stock in stock_list:
        # share = Share(stock)
        stock_price = yf.download(stock, start=today, end=today)
        stock_price = stock_price['Open'].values[0]
        num_of_shares = stock_money / float(stock_price)
        list_of_stock = list_of_prices[count]
        i = 1
        for price in list_of_stock:
            uprice = num_of_shares * price
            s = str(i)
            if (s in dict.keys()):
                dict[s] = dict[s]+ uprice
            else:
                dict[s] = uprice
            i+=1
        count+=1
    return dict

#num_of_months = 5
# low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
#medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
#high_risk_stock_list = ['TSLA', 'AMZN', 'NVDA', 'AAPL']
#list_of_prices = get_list_of_prices(high_risk_stock_list, num_of_months)
# print(list_of_prices)
#money = get_money(high_risk_stock_list, list_of_prices, 50)
# print(money)