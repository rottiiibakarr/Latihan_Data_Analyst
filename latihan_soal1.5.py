import pandas as pd

df = pd.read_csv('data_nilai1.5.csv')

# 1. Removing Duplicates
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih terdapat data duplikat atau tidak!

# 2. Cleaning Empty Cells 
df.dropna(inplace=True)

# 3. Cleaning Wrong Format 
df['Tanggal_Review'] = pd.to_datetime(df['Tanggal_Review'], format='mixed', dayfirst=True)

# 4. Cleaning Wrong Data 
df['Rating_Bintang'] = df['Rating_Bintang'].abs()

# 5. Cleaning Data (Final)
df = df.reset_index(drop=True) # Drop digunakan untuk menghapus index sebelumnya dengan yang baru

print(df.to_string())