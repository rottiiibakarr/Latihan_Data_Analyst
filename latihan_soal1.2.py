import pandas as pd

df = pd.read_csv('data_nilai1.2.csv')

# 1. Removing Duplicates
df.drop_duplicates(inplace=True)

print(df.duplicated()) # Untuk mengecek, apakah masih terdapat data duplikat atau tidak!

# 2. Cleaning Empty Cells
df.dropna(inplace=True)

# 3. Cleaning Wrong Format
df['Tanggal_Input'] = pd.to_datetime(df['Tanggal_Input'], format='mixed', dayfirst=True)
"""
Hasilnya tidak akan terlihat,
karena output dari dropna sebelumnya itu
akan menghapus nilai NaN pada kolom
Konsumsi_Per_Kapita_Kg, jadi untuk hasilnya
itu tidak terlihat!
"""

# 4. Cleaning Wrong Data
for i in df.index :
    if df.loc[i, 'Konsumsi_Per_Kapita_Kg'] < 0 :
        not_negative_konsumsi = df.loc[i, 'Konsumsi_Per_Kapita_Kg']
        df.loc[i, 'Konsumsi_Per_Kapita_Kg'] = abs(not_negative_konsumsi)

"""
Gemini saya mau tanya, 
untuk penggunaan kode seperti ini:
df.loc[i, 'Konsumsi_Per_Kapita_Kg'].abs() 
apakah bisa gak?
"""

# 5. Cleaning Data (Final)
df = df.reset_index(drop=True) 
"""
Indeks lama dihapus dan langsung diganti dengan indeks integer 0, 1, 2....
"""

print(df.to_string())