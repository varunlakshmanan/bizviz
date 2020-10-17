from flask import Flask
from flask import request, jsonify
from revenue_model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/getEstimatedRevenue', methods=['POST'])
def getEstimatedRevenue():
    file_path = request.json['file_path']
    sector = request.json['sector']
    advertising = request.json['advertising']
    wages = request.json['wages']
    fixed_costs = request.json['fixed_costs']
    other_costs = request.json['other_costs']
    online = request.json['online']
    time = request.json['time']
    return jsonify(str(predict(file_path, sector, advertising, wages, fixed_costs, other_costs, online, time)))


if __name__ == '__main__':
    app.run()