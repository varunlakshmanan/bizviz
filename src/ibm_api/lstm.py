from sklearn import preprocessing
import pandas as pd
import keras
import tensorflow as tf
from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation
from keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/stock_data.csv')
stock_list = ['AAPL', 'AMZN', 'TSLA']
count = 1
data_normalizer = preprocessing.MinMaxScaler()
for stock in stock_list:
    stock_data = df.iloc[:, count:count+6]
    count+=6
    stock_data = stock_data.values
    data_normalized = data_normalizer.fit_transform(stock_data)

    len_hist = 50
    #creates time based arrays (every 50 time slots are one)
    ohlcv_histories_normalized = np.array([data_normalized[i:i + len_hist].copy() for i in range(len(data_normalized) - len_hist)])
    #creates time based array of values (answer to 50 time values)
    next_day_open_values_normalized = np.array([data_normalized[:, 0][i + len_hist].copy() for i in range(len(data_normalized) - len_hist)])

    #just convert to proper dimensions
    next_day_open_values_normalized = np.expand_dims(next_day_open_values_normalized, -1)

    #convert actual stock data into array of values to test
    next_day_open_values = np.array([stock_data[:, 0][i + len_hist].copy() for i in range(len(stock_data) - len_hist)])
    next_day_open_values = np.expand_dims(next_day_open_values, -1)

    y_normalizer = preprocessing.MinMaxScaler()
    y_normalizer.fit(next_day_open_values)

    test_split = 0.9
    n = int(ohlcv_histories_normalized.shape[0] * test_split)

    ohlcv_train = ohlcv_histories_normalized[:n]
    y_train = next_day_open_values_normalized[:n]

    ohlcv_test = ohlcv_histories_normalized[n:]
    y_test = next_day_open_values_normalized[n:]


    def lstm():
        lstm_input = Input(name='inputs', shape=(50, 6))
        layer = LSTM(50)(lstm_input)
        layer = Dropout(0.2)(layer)
        layer = Dense(64)(layer)
        layer = Activation('sigmoid')(layer)
        layer = Dense(1)(layer)
        output = Activation('linear')(layer)
        model = Model(inputs=lstm_input, outputs=output)
        return model



    model = lstm()
    adam = optimizers.Adam(lr=0.0005)
    model.compile(optimizer=adam, loss=['mse'])
    model.fit(x=ohlcv_train, y=y_train, batch_size=32, epochs=20, shuffle=True, validation_split=0.1)

    y_test_predicted = model.predict(ohlcv_test)
    y_test_predicted = y_normalizer.inverse_transform(y_test_predicted)
    y_predicted = model.predict(ohlcv_histories_normalized)
    y_predicted = y_normalizer.inverse_transform(y_predicted)

    print(y_test_predicted.shape)
    print(y_predicted.shape)
    print(next_day_open_values.shape)

    real = plt.plot(next_day_open_values[0:-1], label='real')
    pred = plt.plot(y_predicted[0:-1], label='predicted')
    plt.show()
    print(1/0)
