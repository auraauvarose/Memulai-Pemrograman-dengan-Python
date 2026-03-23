"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""


angka_belanja_disco = int(input("masukan angka harga anda:"))

if angka_belanja_disco > 500000:
    total_harga = angka_belanja_disco * 0.9  # mendaatkan potongan 10%
    print(f"anda berhasil mendapatkan diskon 10% jadi: {total_harga}")
else:
    total_harga = angka_belanja_disco # tidak mendapatkan diskon karena tidak lebih dari 500000
    print(f"harga anda adalah: {total_harga}")
