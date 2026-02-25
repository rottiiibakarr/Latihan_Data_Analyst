import pandas as pd 

df = pd.read_csv('data_nilai1.4.csv')

# 1. Removing Duplicates
df.drop_duplicates(inplace=True)
print(df.duplicated()) # Mengecek apakah masih terdapat data duplikat atau tidak

# 2. Cleaning Empty Cells
df.dropna(inplace=True)

# 3. Cleaning Wrong Format 
df['Tanggal_Hadir'] = pd.to_datetime(df['Tanggal_Hadir'], format='mixed', dayfirst=True)

# 4. Cleaning Wrong Data
df['Jam_Kerja'] = df['Jam_Kerja'].abs()

# 5. Cleaning Data
df = df.reset_index(drop=True) # drop digunakan untuk menghapus indeks lama

print(df.to_string())
