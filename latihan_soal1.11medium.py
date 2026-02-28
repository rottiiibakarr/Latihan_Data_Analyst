import pandas as pd 

df = pd.read_csv('data_nilai1.11medium.csv')

# 1. Removing Duplicates:
print(df.duplicated(subset=['Nama_Calon', 'Jalur_Masuk', 'Skor_Ujian', 'Tanggal_Lahir']).sum()) # True: 1
df.drop_duplicates(subset=['Nama_Calon', 'Jalur_Masuk', 'Skor_Ujian', 'Tanggal_Lahir'], inplace=True)

# Cleaning Wrong Format: 
# A
df['Tinggi_Badan_cm'] = df['Tinggi_Badan_cm'].str.replace(' cm', '')


print(df.to_string())