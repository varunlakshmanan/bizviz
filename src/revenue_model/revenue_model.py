import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import GlassRegressor


def preprocess_data(file_path, sector, advertising, wages, fixed_costs, other_costs, online):
    data = pd.read_csv(file_path)
    sectors = {  # from https://www.bls.gov/opub/mlr/2015/article/industry-employment-and-output-projections-to-2024.htm
        'Mining': 0.9,
        'Construction': 1.2,
        'Manufacturing': -0.7,
        'Utilities': -0.9,
        'Wholesale Trade': 0.5,
        'Retail Trade': 0.5,
        'Transportation/Warehousing': 0.3,
        'Information': -0.1,
        'Financial Activities': 0.6,
        'Professional/Business Services': 0.9,
        'Private Education': 0.9,
        'Health Care/Social Assistance': 1.9,
        'Leisure/Hospitality': 0.6,
        'Federal Government': -1.5,
        'State/Local Government': 0.4,
        'Agriculture': -0.5,
        'Other': 0.4
    }
    data['online'] = [1 if item == 'online' else 0 for item in data['online']]
    data['physical'] = [1 if item == 0 else 0 for item in data['online']]
    data['sector'] = sectors[sector]
    features = ['advertising', 'wages', 'fixed_costs', 'other_costs', 'online', 'physical', 'sector']
    X = data[features]
    y = data.revenue

    test_online = 0
    test_physical = 1
    if online == 'online':
        test_online = 1
        test_physical = 0
    test = pd.DataFrame(data={
        'advertising': advertising,
        'wages': wages,
        'fixed_costs': fixed_costs,
        'other_costs': other_costs,
        'online': test_online,
        'physical': test_physical,
        'sector': sectors[sector]
    })
    scaler = MinMaxScaler()
    scaler.fit_transform(X)
    return X, y, test


def train_model(X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    model = GlassRegressor()
    model.fit(X_train, X_val, y_train, y_val, timeout=15, max_in_ensemble=4)
    return model


def predict(file_path, sector, advertising, wages, fixed_costs, other_costs, online, time):
    X, y, test = preprocess_data(file_path, sector, advertising, wages, fixed_costs, other_costs, online)
    model = train_model(X, y)
    for run in range(0, time):
        model.predict(test)
