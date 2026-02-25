import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns 

file_path = 'sales_data.csv'
df = pd.read_csv(file_path, sep=';')

# Konversi kolom tanggal ke format datetime (atau waktu)
df['tanggal'] = pd.to_datetime(df['tanggal'], format='mixed')

# Agregasi data berdasarkan bulan
df_monthly = df.groupby(df['tanggal'].dt.to_period('M')).sum(numeric_only=True)

# Membuat grafik tren penjualan bulanan
plt.figure(figsize=(12,6))
sns.lineplot(x=df_monthly.index.astype(str), y=df_monthly['total_penjualan'], markers='o')
plt.xticks(rotation=45)
plt.xlabel("Bulan")
plt.ylabel('Total Penjualan')
plt.title('Tren Penjualan Bulanan')
plt.show()

# Membuat heatmap korelasi
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Korelasi antar variabel dalam Dataset Penjualan')
plt.show()

