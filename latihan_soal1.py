import pandas as pd

# 1
df = pd.read_csv('data_nilai1.csv')
print(df.to_string())
print("=========================")
print("Jumlah kesalahan")
# Cek jumlah data kosong per kolom
print(df.isnull().sum())

# 2 
df.dropna(subset=['Nama'], inplace=True)
print(df.to_string())   

# 3
mean_nilai_statistika = df['Nilai_Statistika'].mean()
df.fillna({'Nilai_Statistika': mean_nilai_statistika}, inplace=True)
print(df.to_string())

# 4
modus = df['Jurusan'].mode()[0]
df.fillna({'Jurusan': modus}, inplace=True)
print(df.to_string())

# 5
mean_nilai_python = df['Nilai_Python'].mean()
df.fillna({'Nilai_Python': mean_nilai_python}, inplace=True)

df['Nilai_Akhir'] = (df['Nilai_Statistika'] + df['Nilai_Python']) / 2

nilai_lulus = df[df['Nilai_Akhir'] > 80]

if not nilai_lulus.empty :
    print(nilai_lulus.to_string())
else :
    print("Tidak ada mahasiswa yang mempunya nilai lebih dari 80")
