tahun = 2023
penduduk_solo = 150000000  
penduduk_jogja = 120000000 

while penduduk_jogja <= penduduk_solo:
    penduduk_solo += penduduk_solo * 0.10  
    penduduk_jogja += penduduk_jogja * 0.12 
    tahun += 1

print(f"Penduduk kota Yogyakarta akan lebih banyak dari kota Solo pada tahun {tahun}")