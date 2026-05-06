# menghitung total belanja dengan validasi harga dan diskon
total_belanja = int(input("Masukkan jumlah transaksi: "))
total_harga = 0

for i in range(1, total_belanja + 1):
    harga_produk = int(input(f"Masukkan harga barang transaksi ke-{i}: "))
    while harga_produk <= 0:
        print("harga barang tiadak boleh nol atau negatif, masukan ulang!")
        harga_produk = int(input(f"Masukkan harga barang transaksi ke-{i}: "))

    if harga_produk > 150000:
        diskon = 0.20
    elif harga_produk >= 50000:
        diskon = 0.10
    else:
        diskon = 0.0

    harga_akhir = harga_produk - (harga_produk * diskon)
    total_harga += harga_akhir

print(f"total yang harus dibayarkan: Rp{total_harga}")

