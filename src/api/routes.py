from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from src.revenue_model.model import predict
from src.ibm_api.stock_data import get_stock_data_yf
from src.data.fbp import get_list_of_prices,get_money,predict_price
import pandas as pd
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)

@app.route('/')
def home():
    return "Hello World"


@app.route('/getEstimatedRevenue', methods=['POST'])
def get_estimated_revenue():
    file_path = request.json['file_path']
    sector = request.json['sector']
    advertising = request.json['advertising']
    wages = request.json['wages']
    fixed_costs = request.json['fixed_costs']
    other_costs = request.json['other_costs']
    online = request.json['online']
    time = request.json['time']
    return jsonify(str(predict(file_path, sector, advertising, wages, fixed_costs, other_costs, online, time)))

# @app.route('/getPlotData', methods=['GET'])
# def get_plot_data():
#     file_path = request.json['file_path']
#     sector = request.json['sector']
#     advertising = request.json['advertising']
#     wages = request.json['wages']
#     fixed_costs = request.json['fixed_costs']
#     other_costs = request.json['other_costs']
#     online = request.json['online']
#     time = request.json['time']
#     data = pd.read_csv(file_path)
#     dict = dict(zip(data['month'], data['revenue']))
#     X['advertising'].iloc[-1]
#     dict['']

@app.route('/getStockData', methods=['POST'])
def get_stock_data():
    file_path = request.json['file_path']
    sector = request.json['sector']
    advertising = float(request.json['advertising'])
    wages = float(request.json['wages'])
    fixed_costs = float(request.json['fixed_costs'])
    other_costs = float(request.json['other_costs'])
    online = request.json['online']
    time = request.json['time']

    time = int(time)
    money = advertising + wages + fixed_costs + other_costs
    dict = {}
    low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
    medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
    high_risk_stock_list = ['TSLA', 'AMZN', 'NVDA', 'AAPL']
    # get_stock_data_yf(low_risk_stock_list)
    list_of_prices = []
    for stock in low_risk_stock_list:
        with open('../models/'+stock+'.pkl', 'rb') as f:
            model = pickle.load(f)
        list_of_projected = predict_price(stock, model, time)
        list_of_prices.append(list_of_projected)
    low_risk = get_money(stock_list=low_risk_stock_list, list_of_prices=list_of_prices, money=money)
    dict['low_risk'] = low_risk
    list_of_prices = []
    for stock in medium_risk_stock_list:
        with open('../models/' + stock + '.pkl', 'rb') as f:
            model = pickle.load(f)
        list_of_projected = predict_price(stock, model, time)
        list_of_prices.append(list_of_projected)
    medium_risk = get_money(stock_list=medium_risk_stock_list, list_of_prices=list_of_prices, money=money)
    dict['medium_risk'] = medium_risk
    # get_stock_data_yf(medium_risk_stock_list)
    # list_of_prices = get_list_of_prices(medium_risk_stock_list, time)
    # medium_risk = get_money(stock_list=medium_risk_stock_list, list_of_prices=list_of_prices, money=money)
    # dict['medium_risk'] = medium_risk
    list_of_prices = []
    for stock in high_risk_stock_list:
        with open('../models/' + stock + '.pkl', 'rb') as f:
            model = pickle.load(f)
        list_of_projected = predict_price(stock, model, time)
        list_of_prices.append(list_of_projected)
    high_risk = get_money(stock_list=high_risk_stock_list, list_of_prices=list_of_prices, money=money)
    dict['high_risk'] = high_risk
    # get_stock_data_yf(high_risk_stock_list)
    # list_of_prices = get_list_of_prices(high_risk_stock_list, time)
    # high_risk = get_money(stock_list=high_risk_stock_list, list_of_prices=list_of_prices, money=money)
    # dict['high_risk'] = high_risk
    return dict

if __name__ == '__main__':
    app.run()