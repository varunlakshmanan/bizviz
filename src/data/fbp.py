from fbprophet import Prophet
import datetime as dt
from dateutil.easter import easter
import pandas as pd

df = pd.read_csv('../data/stock_data.csv')
stock_list = ['AAPL', 'AMZN', 'TSLA']
count = 1
for stock in stock_list:
    stock_data = df.iloc[:, count:count+7]
    count+=7
    stock_data.to_csv('single_stock_data.csv')
    col_indices = [0,1]
    new_names = ['ds', 'y']
    old_names = stock_data.columns[col_indices]
    stock_data.rename(columns=dict(zip(old_names, new_names)), inplace=True)
    print(stock_data)
    stock_data = stock_data.filter(items=['ds', 'y'])
    print(stock_data)
    model = Prophet(yearly_seasonality=True,)
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    model.fit(stock_data)

    #makes prediction one month in advance
    future_data = model.make_future_dataframe(periods=365)
    forecast = model.predict(future_data)
    fig1 = model.plot(forecast)
    print(forecast)
    print(forecast[['ds', 'yhat']].tail())
    future_data.to_csv('future_data.csv')
    print(1/0)
