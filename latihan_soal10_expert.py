import pandas as pd 

df_users = pd.read_csv('data_nilai10(users)_expert.csv')
df_transaksi = pd.read_csv('data_nilai10(transaksi)_expert.csv')

# 1. Merging Data (Join / Menggabungkan)
df_merge = pd.merge(df_transaksi, df_users, on='User_ID', how='left')

# 2. Missing Values 
df_merge['Nama'] = df_merge['Nama'].fillna('Anonim')
df_merge['Lokasi'] = df_merge['Lokasi'].fillna('Tidak Diketahui')
df_merge['Hobi'] = df_merge['Hobi'].fillna('Tidak Diketahui')

# 3. One-Hot Encoding (String Splitting)
df_merge['Suka_Renang'] = df_merge['Hobi'].str.contains('Renang')

# 4. Date Parsing 
df_merge['Tanggal'] = pd.to_datetime(df_merge['Tanggal'], format='mixed', dayfirst=True)

print(df_merge.to_string())