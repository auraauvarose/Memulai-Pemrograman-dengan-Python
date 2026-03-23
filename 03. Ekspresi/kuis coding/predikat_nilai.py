"""  
TODO: 
Skenario: Dico (si hobi belanja tadi) ternyata juga seorang mahasiswa. Kamu diminta membuat program untuk menentukan Predikat Kelulusan berdasarkan nilai ujiannya.

Ketentuan:
- Program meminta input nilai ujian (0-100).
- Gunakan variabel bernama nilai_ujian.
- Logika Percabangan (if-elif-else):
- Jika nilai 90 ke atas, cetak: "Predikat: A (Istimewa)".
- Jika nilai 75 sampai 89, cetak: "Predikat: B (Sangat Baik)".
- Jika nilai 60 sampai 74, cetak: "Predikat: C (Cukup)".
- Jika di bawah 60, cetak: "Predikat: D (Tidak Lulus)".

"""

nilai_ujian = int(input("masukan nilai ujian: (0-100)"))
if nilai_ujian >= 90:
    print("Predikat: A (Istimewa)")
elif nilai_ujian >= 75:
    print("Predikat: B (Sangat Baik)") 
elif nilai_ujian >= 60:
    print("Predikat: C (Cukup)")
else:
    print("Predikat: D (Tidak Lulus)")