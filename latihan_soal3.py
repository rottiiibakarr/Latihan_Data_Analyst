import pandas as pd 

df = pd.read_csv('data_nilai3.csv')

# 1 Hapus Data Duplikat (Removes Duplicate)
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih ada data duplikat atau gak

# 2 Tambal Harga Kosong (Missing Values)
price_mouse_wireless = df['Harga'].mean()
df.fillna({'Harga': price_mouse_wireless}, inplace=True)

# 3 Perbaiki Format Tanggal ()
df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='mixed', dayfirst=True)

# Koreksi Jumlah Barang (Wrong Data)
for x in df.index :
    if df.loc[x, 'Jumlah'] < 0 :
        values_row = df.loc[x, 'Jumlah']  # Mengambil nilai pada baris tertentu
        df.loc[x, 'Jumlah'] = abs(values_row)

"""
Atau cara lain tanpa looping yaitu df['Jumlah'] = df['Jumlah'].abs()
"""

print(df.to_string())