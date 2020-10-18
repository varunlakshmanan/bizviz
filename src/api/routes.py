from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from src.revenue_model.model import predict
from src.ibm_api.stock_data import get_stock_data_yf
#from src.data.fbp import get_list_of_prices,get_money,predict_price
from src.data.test_fbp import get_list_of_prices,get_money, predict_price
import pandas as pd
import pickle
import datetime
from dateutil.relativedelta import relativedelta

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

    data = pd.DataFrame(file_path)
    data = data.iloc[1:]
    month_year = []
    for index in range(1, len(data['month']) + 1):
        month_year.append(str(data['month'][index]) + str(' ') + str(data['year'][index]))
    # baseline = {}
    baseline = []
    for i in range(0, len(month_year)):
        # baseline[month_year[i]] = data['revenue'][i + 1]
        temp_dict = {}
        curr_date = "1 " + month_year[i]
        d = datetime.datetime.strptime(curr_date, '%d %B %Y')
        s = datetime.datetime.strftime(d, '%m-%d-%Y')
        s += " GMT"
        temp_dict[s] = data['revenue'][i + 1]
        baseline.append(temp_dict)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    last_month = data['month'].iloc[-1]
    next_month = months[(months.index(last_month) + 1) % 12]
    if next_month == 'January':
        next_year = str(int(data['year'].iloc[-1]) + 1)
    else:
        next_year = data['year'].iloc[-1]
    next_month_year = str(next_month) + str(' ') + str(next_year)

    advertising = float(advertising)
    wages = float(wages)
    fixed_costs = float(fixed_costs)
    other_costs = float(other_costs)
    time = float(time)

    projected_revenue = str(predict(file_path, sector, advertising, wages, fixed_costs, other_costs, online, time))
    time = int(time)
    today = "1 " + next_month_year
    d = datetime.datetime.strptime(today, '%d %B %Y')
    d = d + relativedelta(months=(time-1))
    next_month_year = datetime.datetime.strftime(d, '%m-%d-%Y')
    next_month_year += " GMT"
    projection = {next_month_year: projected_revenue}

    dict = {
        'baseline': baseline,
        'projection': projection
    }
    return jsonify(dict)


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
    revenue = 12107.97

    time = int(time)
    money = advertising + wages + fixed_costs + other_costs
    dict = {}
    low_risk_stock_list = ['TDTF', 'BIV', 'PZA']
    medium_risk_stock_list = ['GOOGL', 'URI', 'MSFT']
    high_risk_stock_list = ['AMZN', 'NVDA', 'AAPL']
    # get_stock_data_yf(low_risk_stock_list)
    list_of_prices = []
    for stock in low_risk_stock_list:
        with open('../models/'+stock+'.pkl', 'rb') as f:
            model = pickle.load(f)
        list_of_projected = predict_price(stock, model, time)
        list_of_prices.append(list_of_projected)
    low_risk = get_money(stock_list=low_risk_stock_list, list_of_prices=list_of_prices, money=money)
    dict['low_risk'] = low_risk
    print("Low Risk Portfolio finished...")
    list_of_prices = []
    for stock in medium_risk_stock_list:
        with open('../models/' + stock + '.pkl', 'rb') as f:
            model = pickle.load(f)
        list_of_projected = predict_price(stock, model, time)
        list_of_prices.append(list_of_projected)
    medium_risk = get_money(stock_list=medium_risk_stock_list, list_of_prices=list_of_prices, money=money)
    dict['medium_risk'] = medium_risk
    print("Medium Risk Portfolio finished...")
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
    print(dict)
    return dict

if __name__ == '__main__':
    app.run()