import pandas as pd 

df = pd.read_csv('data_nilai1.3.csv')

# 1. Removing Duplicates 
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih terdapat duplikat atau tidak!

# 2. Cleaning Empty Cells 
df.dropna(inplace=True)

# 3. Cleaning Wrong Format 
df['Tanggal_Transaksi'] = pd.to_datetime(df['Tanggal_Transaksi'], format='mixed', dayfirst=True)

# 4. Cleaning Wrong Data 
df['Jumlah_Beli'] = df['Jumlah_Beli'].abs()
df['Jumlah_Beli'] = df['Jumlah_Beli'].fillna(0)
"""
Mengisi nilai yang kosong dengan 0, 
hasilnya tidak akan terlihat,
karena output dari dropna sebelumnya itu
akan menghapus nilai NaN atau kosong pada kolom
Jumlah_Beli, jadi untuk hasilnya itu tidak terlihat!
"""

# 5. Cleaning Data (Final)
df = df.reset_index(drop=True) # drop digunakan untuk menghapus indeks lama

print(df.to_string())