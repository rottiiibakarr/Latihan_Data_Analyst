import pandas as pd 

df = pd.read_csv('data_nilai1.10medium.csv')

# 1. Removing Duplicates
# A
print(df.duplicated(subset=['Pekerjaan', 'Pengalaman_Tahun', 'Tanggal_Isi']).sum())

# B
df.drop_duplicates(subset=['Pekerjaan', 'Pengalaman_Tahun', 'Tanggal_Isi'], inplace=True)

# 2. Cleaning Wrong Format (Multiple Columns)
# A
df['Pengalaman_Tahun'] = df['Pengalaman_Tahun'].str.replace(' thn', '')

# B
df['Gaji_Bulanan_Juta'] = df['Gaji_Bulanan_Juta'].str.replace('Rp ', '')

# C
df['Pengalaman_Tahun'] = df['Pengalaman_Tahun'].astype(float)
df['Gaji_Bulanan_Juta'] = df['Gaji_Bulanan_Juta'].astype(float)

# D 
df['Tanggal_Isi'] = pd.to_datetime(df['Tanggal_Isi'], format='mixed', dayfirst=True)

print(df.to_string())