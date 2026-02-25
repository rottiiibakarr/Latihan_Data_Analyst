import pandas as pd 

"""
1. Series pada Pandas itu sebagai kolom pada sebuah tabel
2. Label pada Pandas itu sebagai urutan indeks pada sebuah tabel
3. Dataframe pada Pandas itu sebagai keseluruhan pada tabel (termasuk kolom dan urutan)
4. Describe atau Statistik Deskriptif mencakup rata-rata (mean), median, standar deviasi,
   nilai minimum dan maksimum
"""

# mydataset =[1, 7, 2]
# myvar = pd.DataFrame(mydataset, index=['x', 'y', 'z'])
# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3": 390}
# mycalories = pd.Series(calories, index=['day1', 'day2'])
# print(mycalories['day1'])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
mydata = pd.DataFrame(data)
print(mydata)