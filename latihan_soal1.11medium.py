import pandas as pd 

df = pd.read_csv('data_nilai1.11medium.csv')

# 1. Removing Duplicates:
print(df.duplicated(subset=['Nama_Calon', 'Jalur_Masuk', 'Skor_Ujian', 'Tanggal_Lahir']).sum()) # True: 1
df.drop_duplicates(subset=['Nama_Calon', 'Jalur_Masuk', 'Skor_Ujian', 'Tanggal_Lahir'], inplace=True)

# 2. Cleaning Wrong Format: 
# A
df['Tinggi_Badan_cm'] = df['Tinggi_Badan_cm'].str.replace(' cm', '')

# B
df['Tanggal_Lahir'] = pd.to_datetime(df['Tanggal_Lahir'], format='mixed', dayfirst=True)

# 3. Cleaning Wrong Data (Typo Teks):
# A
df['Nama_Calon'] = df['Nama_Calon'].str.title()

# B 
df['Jalur_Masuk'] = df['Jalur_Masuk'].str.upper()

print(df.to_string())