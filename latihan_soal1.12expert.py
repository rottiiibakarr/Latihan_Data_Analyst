import pandas as pd 

# 1. Read Data & Handling Header Spaces (The First Trap):
# A
df = pd.read_csv('data_nilai1.12expert.csv', sep=';')

# B
df.columns = df.columns.str.strip()

print(df.to_string())