import pandas as pd

df = pd.read_csv('data_nilai6_medium.csv')

# Data Cleaning 
# 1. Hapus Data Duplikat (Remove Duplicate)
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih ada data duplikat atau gak

# 2. Imputasi Harga (Missing Value)
median_price_house = df['Harga'].median()
df.fillna({'Harga': median_price_house}, inplace=True)

# 3. Stadardisasi Nama Kota (Incosistent Data)
df['Kota'] = df['Kota'].replace('Bdg', 'Bandung')

# Logika Fisika dan Typo (Wrong Data / Outliers)
for i in df.index :
    # Kasus A 
    if df.loc[i, 'Luas_Tanah'] < 0 :
        not_negative_length = df.loc[i, 'Luas_Tanah']
        df.loc[i, 'Luas_Tanah'] = abs(not_negative_length)
    
    # Kasus B
    if df.loc[i, 'Kamar_Tidur'] > 10 :
        df.loc[i, 'Kamar_Tidur'] = 5

# Tantangan Ekstra (Opsional)
df['Tanggal_Tayang'] = pd.to_datetime(df['Tanggal_Tayang'], format='mixed', dayfirst=True)

print(df.to_string())