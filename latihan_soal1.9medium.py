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
df['Harga_Satuan'] = df['Harga_Satuan'].str.replace('USD ', '')

# B
df['Harga_Satuan'] = df['Harga_Satuan'].astype(float)

# C
df['Tanggal_Masuk'] = pd.to_datetime(df['Tanggal_Masuk'], format='mixed', dayfirst=True)

# 3. Cleaning Wrong Data (Typo Teks & Spasi)
# A
df['Kategori'] = df['Kategori'].str.upper()

# B
df['Nama_Barang'] = df['Nama_Barang'].str.strip() # Untuk menghapus whitespace atau spasi




print(df.to_string())