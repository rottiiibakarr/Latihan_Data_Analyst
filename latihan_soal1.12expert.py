import pandas as pd 

# 1. Read Data & Handling Header Spaces (The First Trap):
# A
df = pd.read_csv('data_nilai1.12expert.csv', sep=';')

# B
df.columns = df.columns.str.strip()

"""
Sebenarnya bisa menggunakan cara seperti dibawah ini: 
df = pd.read_csv('data_nilai1.12expert.csv', sep='\s*;\s*', engine='python')

Penjelasan:
- \s*;\s* adalah sebuah Regex (Regular Expression). 
  Regex adalah semacam bahasa kode untuk mencari pola teks tertentu.
  - \s* (di depan) artinya: "cari spasi, tab, atau karakter kosong apa pun, 
  berapapun jumlahnya (bisa nol atau lebih)".
  - ; artinya: "cari tanda titik koma".
  \s* (di belakang) artinya: "cari lagi spasi, tab, atau karakter kosong 
  apa pun setelah titik koma".
- engine='python'
  -  Mesin c bawaan Pandas tidak mendukung penggunaan separator berupa Regex 
  yang kompleks seperti \s*;\s*. Jika Anda tidak menambahkan engine='python', 
  Pandas biasanya akan memunculkan pesan Warning (peringatan) atau bahkan error.
"""

print(df.to_string())