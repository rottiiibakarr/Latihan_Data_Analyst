import pandas as pd

df = pd.read_csv('data_nilai1.7medium.csv')

# Studi Kasus: Data Reservasi Hotel

# 1. Removing Duplicates
df.drop_duplicates(inplace=True)
print(df.duplicated())

# 2. Cleaning Wrong Format
df['Harga_Per_Malam'] = df['Harga_Per_Malam'].str.replace('Rp ', '')
df['Harga_Per_Malam'] = df['Harga_Per_Malam'].astype(float)

# Soal 1 Medium

# 4. Cleaning Wrong Data
# A
df['Tipe_Kamar'] = df['Tipe_Kamar'].str.title()

# B
# 1.) Tentukan batas harga wajar
batas_maksimal = 2000000 

# 2.) Hitung nilai Median (nilai tengah) HANYA dari harga yang normal (di bawah batas maksimal)
median_harga_normal = df.loc[df['Harga_Per_Malam'] <= batas_maksimal, 'Harga_Per_Malam'].median()

# 3.) Timpa semua harga yang "tidak wajar" (lebih dari 2 juta) dengan nilai median tadi
df.loc[df['Harga_Per_Malam'] > batas_maksimal, 'Harga_Per_Malam'] = median_harga_normal

"""
Cara 1 
# Hitung dulu median (nilai tengah) dari harga yang masuk akal (di bawah 2 juta)
median_harga = df.loc[df['Harga_Per_Malam'] < 2000000, 'Harga_Per_Malam'].median()

# Ubah SEMUA data yang harganya lebih dari 2 juta menjadi nilai median tersebut
df.loc[df['Harga_Per_Malam'] > 2000000, 'Harga_Per_Malam'] = median_harga

Cara 2 
# Bagi 100 untuk semua baris yang harganya di atas 2 juta
df.loc[df['Harga_Per_Malam'] > 2000000, 'Harga_Per_Malam'] = df['Harga_Per_Malam'] / 100
"""

# 3. Cleaning Empty Cells
# Urutannya diubah, dengan menangani Outlier, lalu membersihkan cells kosong dengan mean (AVG)
mean_harga_per_malam = df['Harga_Per_Malam'].mean()
df.fillna({'Harga_Per_Malam': mean_harga_per_malam}, inplace=True)

# 5. Cleaning Data (Final)
df = df.reset_index(drop=True)

print(df.to_string())