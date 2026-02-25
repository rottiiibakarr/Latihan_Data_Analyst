import pandas as pd 

df = pd.read_csv('data_nilai5_medium.csv')

# 1. Hapus Data Duplikat (Removes Duplicates)
df.drop_duplicates(inplace=True)
print(df.duplicated())

# 2. Mengubah Data yang Kosong dengan Median (Missing Values)
median_package_weight = df['Berat_kg'].median()
df.fillna({'Berat_kg': median_package_weight}, inplace=True)

# 3. Mengubah Format Tanggal yang Salah (Wrong Format)
df['Tanggal_Kirim'] = pd.to_datetime(df['Tanggal_Kirim'], format='mixed', dayfirst=True)

# 4. Menangani Outlier dan Data Mustahil (Wrong Data)
for x in df.index :
    # Kasus A (Jarak)
    if df.loc[x, 'Jarak_km'] < 0 :
        not_negative_km = df.loc[x, 'Jarak_km']
        df.loc[x, 'Jarak_km'] = abs(not_negative_km)
    # Kasus B (Berat)
    if df.loc[x, 'Berat_kg'] > 100 :
        value_wrong_data = df.loc[x, 'Berat_kg']
        covert_to_string_without0 = str(int(value_wrong_data)).replace('0', '')
        convert_to_int_without0 = int(covert_to_string_without0)
        df.loc[x, 'Berat_kg'] = convert_to_int_without0

"""
Atau cara lain tanpa looping yaitu df['Jumlah'] = df['Jumlah'].abs()
"""

print(df.to_string())