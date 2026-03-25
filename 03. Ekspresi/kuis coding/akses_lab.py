""" 
TODO: Skenario: Sebagai mahasiswi Informatika, kamu ingin masuk ke Laboratorium Riset AI. Namun, sistem keamanannya memiliki aturan ketat.

Ketentuan:
- Buatlah program yang meminta dua input:
- status_mahasiswa: (Gunakan input string, "aktif" atau "tidak").
- nilai_logika: (Gunakan int(input) angka 0-100).
"""

status_mahasiswa = input("masukan status mahasiswa anda: ")
nilai_logika = int(input("masukan nilai logika angka(0-100)"))

if status_mahasiswa == "aktif" and nilai_logika >= 80:
    print("anda memehuni kreteria: anda masuk.")
elif status_mahasiswa == "nonaktif":
    print("anda tidak diperbolahkan masuk dikarenakan status_mahasiswa anda nonaktif")
else:
    print("sayang sekali anda tidak diperbolahkan masuk dikarenakan nilai anda dibawah 80")



