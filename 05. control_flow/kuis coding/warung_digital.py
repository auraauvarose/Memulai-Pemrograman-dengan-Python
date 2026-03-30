akumulasi_harga = 0

while True:
    print("Menu Warung Digital")
    print("1. Nasi Goreng (Rp 15.000)")
    print("2. Es Teh (Rp 5.000)")
    print("3. Hitung Total & Keluar")
    if akumulasi_harga > 0:
        print("Total Harga: Rp", akumulasi_harga)
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        akumulasi_harga += 15000
    elif pilihan == 2:
        akumulasi_harga += 5000
    elif pilihan == 3:
        print("Total Harga: Rp", akumulasi_harga)
        break