import pandas as pd 

df = pd.read_csv('data_nilai1.10medium.csv')

# 1. Removing Duplicates
# A
print(df.duplicated(subset=['Pekerjaan', 'Pengalaman_Tahun', 'Tanggal_Isi']).sum())

# B
df.drop_duplicates(subset=['Pekerjaan', 'Pengalaman_Tahun', 'Tanggal_Isi'], inplace=True)



print(df.to_string())