# Operasi pada List, Set, dan String

# len() digunakan untuk menghitung panjang dari sebuah list, set dan string
contoh_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contoh_list)
print(len(contoh_list)) # menghitung panjang list

# min/max pada list 
print(min(contoh_list))
print(max(contoh_list))

#count 
contoh_count = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5]
string_count = "ada berapa huruf a"
print(contoh_count.count(1)) # ada berapa angka 1 di dalam list
print(string_count.count("a")) # ada berapa huruf a

# in & not in - Cek keberadaan
print('Dicoding' in string_count)    # True
print('tidak' not in string_count)  # True

# Multiple assignment
data = ['shirt', 'white', 'L']
apparel, color, size = data
print(apparel, color, size)  # Output: shirt white L

# sort() - Urutkan (hanya untuk tipe data homogen)
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()  # Ascending
print(kendaraan)  # ['helikopter', 'mobil', 'motor', 'pesawat']

kendaraan.sort(reverse=True)  # Descending
print(kendaraan)  # ['pesawat', 'motor', 'mobil', 'helikopter']

# Untuk case-insensitive sort:
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=str.lower)
print(kendaraan)  # ['helikopter', 'mobil', 'motor', 'Pesawat']