import pandas as pd 

df = pd.read_csv('data_nilai1.11medium.csv')

# 1. Removing Duplicates:
print(df.duplicated(subset=['Nama_Calon', 'Jalur_Masuk', 'Skor_Ujian', 'Tanggal_Lahir']).sum()) # True: 1
df.drop_duplicates(subset=['Nama_Calon', 'Jalur_Masuk', 'Skor_Ujian', 'Tanggal_Lahir'], inplace=True)

# 2. Cleaning Wrong Format: 
# A
df['Tinggi_Badan_cm'] = pd.to_numeric(df['Tinggi_Badan_cm'].str.replace(' cm', '')) 

# B
df['Tanggal_Lahir'] = pd.to_datetime(df['Tanggal_Lahir'], format='mixed', dayfirst=True)

# 3. Cleaning Wrong Data (Typo Teks):
# A
df['Nama_Calon'] = df['Nama_Calon'].str.title()

# B 
df['Jalur_Masuk'] = df['Jalur_Masuk'].str.upper()


# 4. Cleaning Wrong Data (Logika & Outlier):
# A 
df['Skor_Ujian'] = df['Skor_Ujian'].abs()

# B
maksimal_tinggi_badan = 220 
mean_tinggi_badan = df.loc[df['Tinggi_Badan_cm'] <= maksimal_tinggi_badan, 'Tinggi_Badan_cm'].mean()
df.loc[df['Tinggi_Badan_cm'] > maksimal_tinggi_badan, 'Tinggi_Badan_cm'] = mean_tinggi_badan

# 5. Cleaning Empty Cells:
# A
median_skor_ujian = df['Skor_Ujian'].median()
df.fillna({'Skor_Ujian': median_skor_ujian}, inplace=True)

# B 
mean_tinggi_badan = df.loc[df['Tinggi_Badan_cm'] <= maksimal_tinggi_badan, 'Tinggi_Badan_cm'].mean()
"""
Disini saya memanggil lagi 'mean_tinggi_badan', kenapa? 

Karena hasil dari nilai yang lebih besar dari 'maksimal_tinggi_badan' itu saya isi dengan
'mean_tinggi_badan' awal, yang dimana saya ganti dulu nilai yang lebih besar dari 'maksimal_tinggi_badan'
dengan 'mean_tinggi_badan', lalu setelah diganti, saya panggi lagi variabel 
mean_tinggi_badan = df['Tinggi_Badan_cm'].mean() tersebut, karena nilai yang lebih besar dari
'maksimal_tinggi_badan' sudah diganti dengan yang baru, yaitu 'mean_tinggi_badan', lalu setelah
diganti, lakukan mean ulang secara kesuluruhan (termasuk yang baru) untuk mengisi nilai yang kosong (NaN)
dengan mean (rata-rata).
"""
df.fillna({'Tinggi_Badan_cm': mean_tinggi_badan}, inplace=True)

# 6. Cleaning Data (Final): 
df = df.reset_index(drop=True)

print(df.to_string())