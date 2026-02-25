import pandas as pd 

df = pd.read_csv('data_nilai2.csv')

print(df.to_string())

# 1 Removing Duplicates 
df.drop_duplicates(inplace=True)

print(df.duplicated()) # Mengecek apakah masih terdapat duplikat atau tidak

# 2 Wrong Format 
df['Tanggal_Ujian'] = pd.to_datetime(df['Tanggal_Ujian'], format='mixed')

print(df.to_string())

# 3 Wrong Data 
for x in df.index: 
    if df.loc[x, 'Nilai_Python'] > 100:
        df.loc[x, 'Nilai_Python'] = 100

print(df.to_string()) # Mengecek apakah masih terdapat data yang salah atau tidak
