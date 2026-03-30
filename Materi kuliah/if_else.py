
usia = 10

if(usia >= 17):
    print("12 tahun keatas, sudah dewasa")
    tiket = 100000
else:
    print("dibawah 17 tauhn")
    tiket = 50000
    
print("harga tiket anda: ", tiket)

# ini adalah cara kerja input dan output

nilai_stdandar = input("masukan nilai standar: (0-100)")
nilai_siswa = input("masukan nilai sisawa: (0-100)")

if nilai_siswa > nilai_stdandar:
    print("selamat anda lulus")
else:    
    print("maaf anda tidak lulus")
    
# jika nilai siswa 0 atau diatas 100, atau tidak diinput maka ada error 

nilai = int(input("masukan nilai anda: "))

# 1. Cek apakah nilai di luar jangkauan (0-100)
if nilai < 0 or nilai > 100:
    print("nilai yang anda input diluar dari range 0-100")
else:
    # 2. Jika nilai aman, kita cek gradenya dari atas ke bawah
    if nilai >= 80: # nilai 81-100 = A
        print("Nilai anda A")
    elif nilai >= 70: # nilai 71-79 = B
        print("nilai anda B")
    elif nilai >= 60: # nilai 61-79 = C
        print("nilai anda C")
    elif nilai >= 40: # nilai 41-59 = D
        print("nilai anda D")
    elif nilai >= 0 and nilai <= 39: # nilai 1-39 = E
        print("nilai anda E")
    else:
        # Cadangan jika ada input aneh
        print("nilai anda terlalu rendah, perbaiki ya..")
    


