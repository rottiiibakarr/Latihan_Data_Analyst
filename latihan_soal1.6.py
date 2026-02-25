import pandas as pd

df = pd.read_csv('data_nilai1.6.csv')

# 1. Removing Duplicates 
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih terdapat data duplikat atau tidak!

# 2. Cleaning Empty Cells
df.dropna(inplace=True)

# 3. Cleaning Wrong Format 
df['Tanggal_Pinjam'] = pd.to_datetime(df['Tanggal_Pinjam'], format='mixed', dayfirst=True)

# 4. Cleaning Wrong Data 
df['Lama_Pinjam_Hari'] = df['Lama_Pinjam_Hari'].abs()

# 5. Cleaning Data (Final)
df = df.reset_index(drop=True)

print(df.to_string())