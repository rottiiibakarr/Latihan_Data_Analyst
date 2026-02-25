import pandas as pd 

df = pd.read_csv('data_nilai7_ujian.csv')

# 1. Hapus Duplikat 
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masi terdapat data duplikat atau tidak

# 2. Imputasi Umur 
median_age = df['Umur'].median()
df.fillna({'Umur': median_age}, inplace=True)

# 3. Standarisasi Tanggal
df['Tanggal_Daftar'] = pd.to_datetime(df['Tanggal_Daftar'], format='mixed', dayfirst=True)

# Soal No 4 - 6
for i in df.index :
    # 4. Koreksi Detak Jantung 
    if df.loc[i, 'Detak_Jantung'] < 0 :
        not_minus_heart_rate = df.loc[i, 'Detak_Jantung']
        df.loc[i, 'Detak_Jantung'] = abs(not_minus_heart_rate)
    
    # 5. Handling Outlier Umur 
    if df.loc[i, 'Umur'] > 100 :
        df.loc[i, 'Umur'] = df.loc[i, 'Umur'] // 10 # Dibulatkan, biar output yang dihasilkan tidak negatif

    # 6. Standarisasi Gender
    # A
    if df.loc[i, 'Gender'].islower() :
        df.loc[i, 'Gender'] = df.loc[i, 'Gender'].upper()
    
    # B 
    if df.loc[i, 'Gender'] == 'Perempuan' :
        df.loc[i, 'Gender'] = 'P'
        
    


print(df.to_string())