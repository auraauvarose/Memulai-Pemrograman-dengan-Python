""" 
Kontrol Perulangan
Selain membuat perulangan, kita juga dapat mengontrol perulangan dengan menggunakan beberapa pernyataan di antaranya sebagai berikut.

"""

# Break 
""" Break
Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya. Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan sesuai dengan tingkatan atau letak perulangannya berada.

"""
for i in range(10):
    if i == 5:
        break
    print(i)
    
# contoh lain
print()
for i in range(2): # perulangan tingkat pertama 
    print("perulangan luar: ", i)
    for j in range(10): # perulangan tingkat kedua
        print("perulangan dalam: ", j)
        if j == 1:
            break # Menghentikan perulangan dalam jika j = 1
        
# contoh lain 
print()
for huruf in "Dico ding":
    if huruf == ' ':
        break
    print("huruf saat ini: {}" .format(huruf))
    
    
# Continue
""" Continue
Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.

"""

print()
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
    

# else setelah for
""" Else setelah For
Pada Python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian. Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.

"""

numbers = [1,2,3,4,5]

print()
for num in numbers:
    if num == 6:
        print("Angka ditemmukan program berhenti")
        break;
else:
    print("angka tidak ditemukan ")