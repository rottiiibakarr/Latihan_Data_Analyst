import pandas as pd 

df = pd.read_csv('data_nilai8_expert.csv')

# 1. Membersihkan Format Uang (String Parsing)
cols = ['Saldo_Awal', 'Saldo_Akhir']
for col in cols :
    df[col] = df[col].astype(str).str.replace('Rp ', '').str.replace('.', '')
    df[col] = pd.to_numeric(df[col]) # Dikonversi dari String ke Integer

# 2. Imputasi Logika
df['Transaksi'] = df['Transaksi'].fillna(df['Saldo_Akhir'] - df['Saldo_Awal'])

# 3. Validasi dan Koreksi Data (Audit)
# df['Transaksi'] = df['Transaksi'].abs() # Memutlakan Nilai supaya tidak Negatif pada nilai Transaksi
# df['Transaksi'] = df['Transaksi'].astype(int) # Mengubah supaya tidak float
audit_salah = (df['Saldo_Awal'] + df['Transaksi']) != df['Saldo_Akhir']
df.loc[audit_salah, 'Saldo_Akhir'] = df['Saldo_Awal'] + df['Transaksi']


# Misi Tambahan
df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='mixed', dayfirst=True)

print(df.to_string())   