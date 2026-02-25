import pandas as pd 

df = pd.read_csv('data_nilai1.1.csv')

df.drop_duplicates(inplace=True)

print(df.duplicated()) # untuk mengecek, apakah masih ada data yang duplikat atau

print(df.to_string())