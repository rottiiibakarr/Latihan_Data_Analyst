import pandas as pd

df = pd.read_csv('data_nilai1.9medium.csv')

# Soal 3 Medium (Pro)

# 1. Removing Duplicates
# A 
print(df.duplicated().sum())

# B
df.drop_duplicates(inplace=True)

# 2. Cleaning Wrong Format
# A
df['Harga_Satuan'] = df['Harga_Satuan'].str.replace('USD ', '')

# B
df['Harga_Satuan'] = df['Harga_Satuan'].astype(float)

# C
df['Tanggal_Masuk'] = pd.to_datetime(df['Tanggal_Masuk'], format='mixed', dayfirst=True)

# 3. Cleaning Wrong Data (Typo Teks & Spasi)
# A
df['Kategori'] = df['Kategori'].str.upper()

# B
df['Nama_Barang'] = df['Nama_Barang'].str.strip() # Untuk menghapus whitespace atau spasi

# 4. Cleaning Wrong Data (Logical Error & Outlier)
# A (Logika)
df['Stok'] = df['Stok'].abs() # Mengubah nilai negatif ke positif

# B (Outlier)
batas_maksimal = 1000

"""
Langkah 1, 
Cari terlebih dahulu baris pada kolom 'Stok' dengan nilai dibawah 'batas_maksimal',
Langkah 2,
Jika sudah menemukan nilai dibawah 'batas_maksimal', selanjutnya yaitu menghitung 
nilai tersebut dengan menggunakan Median (nilai tengah),
Langkah 3,
Jika sudah dihitung dengan nilai Median nya, selanjutnya yaitu mencari baris pada 
kolom 'Stok' dengan nilai diatas 'batas_maksimal',
Langkah 4,
Jika sudah menemukan nilai yang lebih besar dari 'batas_maksimal', selanjutnya yaitu 
memberikan nilai baru dengan variabel sebelumnya 'median_stok', dengan mengganti nilai
sebelumnya yaitu 8000pcs menjadi 1000pcs (tidak pakai pcs aslinya) berdasarkan nilai 
median dari seluruh baris kolom 'Stok'.
"""
median_stok = df.loc[df['Stok'] <= batas_maksimal, 'Stok'].median()
df.loc[df['Stok'] > batas_maksimal, 'Stok'] = median_stok

# 5. Cleaning Empty Cells (Multiple Imputation)
# A
df.fillna({'Stok': 0}, inplace=True)

# B
mean_harga_satuan = df['Harga_Satuan'].mean()
df.fillna({'Harga_Satuan': mean_harga_satuan}, inplace=True)

# 6. Cleaning Data (Final & Validasi)
# A
df = df.reset_index(drop=True)

# B
"""
Ketika di print, tipe data pada kolom 'Stok' yang seharusnya sudah diubah sebelumnya dari
float ke int, akan berubah ke tipe data awal yaitu 'float', hal ini dikarenakan saya melakukan
perubahan tipe data pada kolom 'Stok' itu setelah print(df.tail(1)), bukan sebelumnya, yang 
menghasilkan output tipe data yang masih belum diubah. 
"""
print(df.tail(1)) 

# C
"""
Output yang ditampilkan setelah print(df.info()) seperti ini:
RangeIndex: 6 entries, 0 to 5
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   ID_Barang      6 non-null      object
 1   Nama_Barang    6 non-null      object
 2   Kategori       6 non-null      object
 3   Stok           6 non-null      float64
 4   Harga_Satuan   6 non-null      float64
 5   Tanggal_Masuk  6 non-null      datetime64[ns]
dtypes: datetime64[ns](1), float64(2), object(3)
memory usage: 420.0+ bytes

dan seandainya jika diubah sebelumn print(df.info()) akan seperti ini:
RangeIndex: 6 entries, 0 to 5
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   ID_Barang      6 non-null      object
 1   Nama_Barang    6 non-null      object
 2   Kategori       6 non-null      object
 3   Stok           6 non-null      int64
 4   Harga_Satuan   6 non-null      float64
 5   Tanggal_Masuk  6 non-null      datetime64[ns]
dtypes: datetime64[ns](1), float64(1), int64(1), object(3)
memory usage: 420.0+ bytes

akan mendapatkan perbedaan Dtype pada kolom 'Stok'
"""
print(df.info())

# Opsional
"""
Perbaikan tambahan pada kolom 'stok', karena kolom 'stok' sebelumnya itu menggunakan tipe
data float, pada dasarnya 'stok' itu termasuk data diskrit, hal ini dikarenakan data 'stok'
diperoleh melalui hasil penghitungan (bukan pengukuran), dimana nilainya berbentuk bilangan
bulat (int) dan terpisah, tidak mungkin ada 'stok' barang yang berjumlah setengah atau desimal.
"""
df['Stok'] = df['Stok'].astype(int)


print(df.to_string())