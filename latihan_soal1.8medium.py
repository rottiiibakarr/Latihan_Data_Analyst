import pandas as pd 

df = pd.read_csv('data_nilai1.8medium.csv')

# Soal 2 Medium

# 1. Removing Duplicates 
df.drop_duplicates(inplace=True)
print(df.duplicated()) 

# 2. Cleaning Wrong Format
df['Berat_Barang'] = df['Berat_Barang'].str.replace(' kg', '')
df['Berat_Barang'] = df['Berat_Barang'].astype(float)

# 3 Cleaning Wrong Data (Typo Teks)
df['Status'] = df['Status'].str.title()

# 4. Cleaning Wrong Data (Outlier)
maksimal = 100 # Untuk menentukan berat maksimal pada berat barang paket
"""
Langkah 1,
cari terlebih dahulu bari pada kolo Berat_Barang dengan nilai dibawah maksimal, 
Langkah 2,
Jika sudah menemukan dimana nilai dibawah maksimal, lalu hitung dengan menggunakan median,
Langkah 3,
Jika sudah dihitung menggunakan median, selanjutnya cari baris pada kolom Berat_Barang yang
nilainya lebih dari Maksimal
Langkah 4,
Jika sudah menemukan nilai yang lebih dari Maksimal, lalu berikan nilai baru dengan variabel
baru sebelumnya yaitu median_berat_barang, dengan menimpa nilai sebelumnya yaitu 5000kg menjadi
1.75kg berdasarkan nilai median dari seluruh baris pada kolom Berat_Barang
"""
median_berat_barang = df.loc[df['Berat_Barang'] <= maksimal, 'Berat_Barang'].median() 
df.loc[df['Berat_Barang'] > maksimal, 'Berat_Barang'] = median_berat_barang

# 5. Cleaning Empty Cells
mean_ongkos_kirim = df['Ongkos_Kirim'].mean()
df.fillna({'Ongkos_Kirim': mean_ongkos_kirim}, inplace=True)

# 6. Cleaning Data (Final)
df = df.reset_index(drop=True) # Menghapus index lama dengan index yang baru

print(df.to_string())