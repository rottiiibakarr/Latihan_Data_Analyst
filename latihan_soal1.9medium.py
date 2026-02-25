import pandas as pd

df = pd.read_csv('data_nilai1.9medium.csv')

# Soal 3 Medium (Pro)

# 1. Removing Duplicates
# A 
print(df.duplicated().sum())

# B
df.drop_duplicates(inplace=True)

# 2. Cleaning Wrong Format
# A
df['Harga_Satuan']

print(df.to_string())