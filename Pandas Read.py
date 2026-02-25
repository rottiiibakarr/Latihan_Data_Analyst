import pandas as pd 

pd.options.display.max_rows = 999
df = pd.read_csv('data.csv')

print(df.to_string())
# print(df)
# print(pd.options.display.max_rows)