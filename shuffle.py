import pandas as pd

df = pd.read_csv('offers.csv', header=None)
ds = df.sample(frac=1)
ds.to_csv('newoffers.csv')
