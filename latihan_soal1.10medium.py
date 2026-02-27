import pandas as pd 

df = pd.read_csv('data_nilai1.10medium.csv')

# 1. Removing Duplicates
# A
print(df.duplicated(subset=['Pekerjaan', 'Pengalaman_Tahun', 'Tanggal_Isi']).sum())

# B
df.drop_duplicates(subset=['Pekerjaan', 'Pengalaman_Tahun', 'Tanggal_Isi'], inplace=True)

# 2. Cleaning Wrong Format (Multiple Columns)
# A
df['Pengalaman_Tahun'] = df['Pengalaman_Tahun'].str.replace(' thn', '')

# B
df['Gaji_Bulanan_Juta'] = df['Gaji_Bulanan_Juta'].str.replace('Rp ', '')

# C
df['Pengalaman_Tahun'] = df['Pengalaman_Tahun'].astype(float)
df['Gaji_Bulanan_Juta'] = df['Gaji_Bulanan_Juta'].astype(float)

# D 
df['Tanggal_Isi'] = pd.to_datetime(df['Tanggal_Isi'], format='mixed', dayfirst=True)

# 3. Cleaning Wrong Data (Typo Teks Super Berantakan)
# A
df['Pekerjaan'] = df['Pekerjaan'].str.title()

# B
df['Kota_Domisili'] = df['Kota_Domisili'].str.strip().str.title()


# 5. Cleaning Empty Cells (Logika Domain):
# A 
maksimal_pengalaman_tahun = 40
median_pengalaman_tahun = df.loc[df['Pengalaman_Tahun'] <= maksimal_pengalaman_tahun, 'Pengalaman_Tahun'].median()

df.fillna({'Pengalaman_Tahun': median_pengalaman_tahun}, inplace=True)

# B
mean_gaji_bulanan = df['Gaji_Bulanan_Juta'].mean()
df.fillna({'Gaji_Bulanan_Juta': mean_gaji_bulanan}, inplace=True)

"""
Penjelasan:
Untuk tugas 5 saya dahulukan terlebih dahulu dari tugas 4, karena pada tugas 5 saya harus mengisi
nilai kosong (NaN) tersebut dengan nilai median, lalu diisi dengan kolom 'Pengalaman_Tahun' dengan
variabel 'median_penglaman_tahun', kalo tidak didahulukan, perhitungannya akan tidak sesuai.
"""

# 4. Cleaning Wrong Data (Logical Error & Outlier):
# A
df['Pengalaman_Tahun'] = df['Pengalaman_Tahun'].abs()

# B
df.loc[df['Pengalaman_Tahun'] > maksimal_pengalaman_tahun, 'Pengalaman_Tahun'] = median_pengalaman_tahun

# 6. Cleaning Data (Final):
# A 
df = df.reset_index(drop=True)

# B
print(df.info())
"""
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 6 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   ID_Survei          6 non-null      object
 1   Pekerjaan          6 non-null      object
 2   Pengalaman_Tahun   6 non-null      float64
 3   Gaji_Bulanan_Juta  6 non-null      float64
 4   Kota_Domisili      6 non-null      object
 5   Tanggal_Isi        6 non-null      datetime64[ns]
dtypes: datetime64[ns](1), float64(2), object(3)
memory usage: 420.0+ bytes
None
"""

print(df.to_string())

"""
Catatan:
Untuk tugas 5A, untuk pengalaman tahun tidak saya konversi tipe data ke int ya, karena saya memenuhi 
tugas 2C, dengan mempertahankan tipe data float.
"""
