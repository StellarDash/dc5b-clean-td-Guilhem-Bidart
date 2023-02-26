import pandas as pd

file = pd.read_csv('parse.csv', usecols=[1, 2, 10])
file = file.dropna()
file = file[file['Series_title_2'].isin(['Credit', 'Debit', 'Services'])]
file = file.reset_index(drop=True)
file.to_csv('result.csv', index_label='ID', columns=['Period', 'Data_value', 'Series_title_2'])
