import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from revenue_model.GlassRegressor import GlassRegressor


def preprocess_data(file_path, sector, advertising, wages, fixed_costs, other_costs, online):
    data = pd.DataFrame(file_path)
    data = data.iloc[1:]
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
    data['online'] = [1 if item == 'Online' else 0 for item in data['online']]
    data['physical'] = [1 if item == 0 else 0 for item in data['online']]
    data['sector'] = sectors[sector]
    features = ['advertising', 'wages', 'fixed_costs', 'other_costs', 'online', 'physical', 'sector']
    X = data[features]
    y = data.revenue

    test_online = 0
    test_physical = 1
    if online == 'Online':
        test_online = 1
        test_physical = 0
    test = pd.DataFrame(data={
        'advertising': float(advertising),
        'wages': float(wages),
        'fixed_costs': float(fixed_costs),
        'other_costs': float(other_costs),
        'online': float(test_online),
        'physical': float(test_physical),
        'sector': float(sectors[sector])
    }, index=[0])
    scaler = RobustScaler()
    scaler.fit_transform(X)
    return X, y, test


def train_model(X, y, timeout):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    X_train.to_csv("test.csv")
    model = GlassRegressor()
    model.fit(X_train, y_train, X_val, y_val, timeout, max_in_ensemble=4)
    return model


def extrapolate_costs(X, time):
    advertising_slope = (float(X['advertising'].iloc[-1]) - float(X['advertising'].iloc[0])) / float(len(X['advertising']))
    advertising_extrapolation = float(X['advertising'].iloc[-1]) + (float(time) * advertising_slope)
    wages_slope = (float(X['wages'].iloc[-1]) - float(X['wages'].iloc[0])) / float(len(X['wages']))
    wages_extrapolation = float(X['wages'].iloc[-1]) + (float(time) * wages_slope)
    fixed_costs_slope = (float(X['fixed_costs'].iloc[-1]) - float(X['fixed_costs'].iloc[0])) / float(len(X['fixed_costs']))
    fixed_costs_extrapolation = float(X['fixed_costs'].iloc[-1]) + (float(time) * fixed_costs_slope)
    other_costs_slope = (float(X['other_costs'].iloc[-1]) - float(X['other_costs'].iloc[0])) / float(len(X['other_costs']))
    other_costs_extrapolation = float(X['other_costs'].iloc[-1]) + (float(time) * other_costs_slope)
    online_extrapolation = float(X['advertising'].iloc[-1])
    sector_slope = (float(X['sector'].iloc[-1]) - float(X['sector'].iloc[0])) / float(len(X['sector']))
    sector_extrapolation = float(X['sector'].iloc[-1]) + (float(time) * sector_slope)
    if online_extrapolation == 'online':
        physical_extrapolation = 0
    else:
        physical_extrapolation = 1
    extrapolated_data = pd.DataFrame(data={
        'advertising': float(advertising_extrapolation),
        'wages': float(wages_extrapolation),
        'fixed_costs': float(fixed_costs_extrapolation),
        'other_costs': float(other_costs_extrapolation),
        'online': float(online_extrapolation),
        'physical': float(physical_extrapolation),
        'sector': float(sector_extrapolation)
    }, index=[0])
    return extrapolated_data


def predict(file_path, sector, advertising, wages, fixed_costs, other_costs, online, time, timeout=1):
    advertising = float(advertising)
    wages = float(wages)
    fixed_costs = float(fixed_costs)
    other_costs = float(other_costs)
    time = float(time)
    X, y, test = preprocess_data(file_path, sector, advertising, wages, fixed_costs, other_costs, online)
    model = train_model(X, y, timeout)
    if time == 1:
        return float(model.predict(test)[0])
    else:
        print(float(model.predict(extrapolate_costs(X, time))[0]))
        return float(model.predict(extrapolate_costs(X, time))[0])

