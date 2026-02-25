import pandas as pd

df = pd.read_csv('data_nilai11_expert.csv')

# Hapus Duplikat
print(df.duplicated())