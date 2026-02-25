import pandas as pd 

df = pd.read_csv('data_nilai4.csv')

# 1. Menghapus Data Duplikat (Removes Duplicates)
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih terdapat duplikasi data atau gak

# 2. Data Hilang (Missing Value)
employees_salary = df['Gaji'].mean()
df.fillna({'Gaji': employees_salary}, inplace=True)

# Ubah Format Tanggal (Wrong Format)
df['Tanggal_Masuk'] = pd.to_datetime(df['Tanggal_Masuk'], format='mixed')

# Mengubah Data yang Salah (Wrong Data)
for x in df.index :
    if df.loc[x, 'Jam_Kerja'] > 24 :
        df.loc[x, 'Jam_Kerja'] = 8

print(df.to_string())