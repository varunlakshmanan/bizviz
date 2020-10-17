import pandas as pd
import sklearn
import keras

def preprocess_data(file_path, sector):
    data = pd.read_csv(file_path)
    sectors = { # from https://www.bls.gov/opub/mlr/2015/article/industry-employment-and-output-projections-to-2024.htm
        'Mining' : 0.9,
        'Construction' : 1.2,
        'Manufacturing' : -0.7,
        'Utilities' : -0.9,
        'Wholesale Trade' : 0.5,
        'Retail Trade' : 0.5,
        'Transportation/Warehousing' : 0.3,
        'Information' : -0.1,
        'Financial Activities' : 0.6,
        'Professional/Business Services' : 0.9,
        'Private Education' : 0.9,
        'Health Care/Social Assistance' : 1.9,
        'Leisure/Hospitality' : 0.6,
        'Federal Government' : -1.5,
        'State/Local Government' : 0.4,
        'Agriculture' : -0.5,
        'Other' : 0.4
    }
    data['online'] = [1 if item == 'online' else 0 for item in data['online']]
    data['physical'] = [1 if item == 0 else 0 for item in data['online']]
    data['sector'] = sectors[sector]
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit_transform(data)
    return data

def train_model(data):
    features = ['advertising', 'wages', 'fixed_costs', 'other_costs', 'online', 'physical', 'sector']
    X = data[features]
    y = data.revenue


def evaluate(model):


def predict(file_path, business_type, sector, twime):
    data = preprocess_data(file_path, business_type, sector)
    model = train_model(data)
    for run in range(0, time):
        evaluate(model)
