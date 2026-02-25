import pandas as pd
import numpy as np

df = pd.read_csv('data_nilai9_expert.csv')

# 1. Cleaning Strings 
df['Barang_Masuk'] = df['Barang_Masuk'].str.replace(r'\D', '', regex=True)

# 2. Handling Missing Values & Duplicates
# Delete Duplikat
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih ada duplikat atau gak

# Missing Values
# Sudah dilakukan pada nomor 4, Tugas A (Audit)

# 3. Feature Extraction
df['Kategori'] = df['Kode_Barang'].str[:2]

# 4. Validasi Stok
# Tugas A: Audit
cols = ['Stok_Awal', 'Barang_Masuk', 'Barang_Keluar']
for col in cols :
    df[col] = pd.to_numeric(df[col], errors='coerce')

df[cols] = df[cols].fillna(0) # Untuk nomor 2, bagian Missing Value

revisi_stok_akhir = (df['Stok_Awal'] + df['Barang_Masuk']) - df['Barang_Keluar']

kondisi_stok_akhir = [
    (revisi_stok_akhir < 0),
    (revisi_stok_akhir != df['Stok_Akhir'])
]

perbaikan_stok_akhir = [
    0,
    revisi_stok_akhir # Tugas B: Perbaikan Tipe Nilai pada Stok Akhir
]

df['Stok_Akhir'] = np.select(kondisi_stok_akhir, perbaikan_stok_akhir, default=df['Stok_Akhir'])    

# 6. Konversi Waktu (datetime)
df['Tanggal_Cek'] = pd.to_datetime(df['Tanggal_Cek'], format='mixed', dayfirst=True)

print(df.to_string())