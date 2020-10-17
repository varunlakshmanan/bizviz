import requests
import pandas as pd

csv = requests.get('https://raw.githubusercontent.com/IBM/watson-stock-market-predictor/master/data/AAPL.csv')
df = pd.read_csv('https://raw.githubusercontent.com/IBM/watson-stock-market-predictor/master/data/AAPL.csv', index_col=0)

df.to_csv('AAPL.csv')
