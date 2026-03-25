# membuat kalulator sederhana

print("Selamat datang di kalkulator sederhana")
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukan pilihan (1/2/3/4): ")

angka1 = float(input("Masukan angka pertama: "))
angka2 = float(input("Masukan angka kedua: "))

if pilihan == "1":
    hasil = angka1 + angka2
    print("Hasil penjumlahan adalah:", hasil)
elif pilihan == "2":
    hasil = angka1 - angka2
    print("Hasil pengurangan adalah:", hasil)
elif pilihan == "3":
    hasil = angka1 * angka2
    print("Hasil perkalian adalah:", hasil)
elif pilihan == "4":
    hasil = angka1 / angka2
    print("Hasil pembagian adalah:", hasil)
else:
    print("Pilihan tidak valid")