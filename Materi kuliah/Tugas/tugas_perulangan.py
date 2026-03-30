'''
TUGAS KELAS:
Buatlah program yang meminta pengguna untuk memasukkan angka. 
Program akan terus meminta pengguna memasukkan angka, kecuali jika yang diinput adalah angka 0. 
Setelah menekan angka 0, program berhenti lalu menampilkan jumlah total dari angka-angka yang sebelumnya telah dimasukkan.
'''

total = 0

while True: # membuat agar while nilai nya true
    angka = int(input("masukan angka: "))
    total += angka
    if angka == 0:
        break

print("total: ", total)
    