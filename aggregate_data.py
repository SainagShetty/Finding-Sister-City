import pandas as pd

cityDt = pd.read_csv('edited-list.csv',sep=',')
proDt = pd.read_csv('data gathering/proximity/data/proximity_2.csv')

tmp = pd.merge(cityDt, proDt, on='id')
tmp.to_csv('city-list-with-proximity.csv',sep=',')

