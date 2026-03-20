# ====== 1. Mengubah Huruf Besar/Kecil ====== 

kata = 'dikoding'
kata = kata.upper() # menggunakan metode lower()
print(kata) # kata men adi besar


kata = 'DIKODING' # menggunakan metode upper()
kata = kata.lower()
print(kata)


# ====== 2. Menghapus Whitespace atau Karakter ======
print("Dicoding          ".rstrip())      # Output: Dicoding
print("           Dicoding".lstrip())     # Output: Dicoding
print("         Dicoding          ".strip())  # Output: Dicoding

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))  # Output: Dicoding

# ====== 3. Pengecekan Awal/Akhir String ======
print('Dicoding Indonesia'.startswith('Dicoding'))  # Output: True
print('Dicoding Indonesia'.endswith('Dicoding'))    # Output: False

# ====== 4. Gabung & Pisah String ======
print(' '.join(['Dicoding','Indonesia', '!']))     # Output: Dicoding Indonesia !
print('123'.join(['Dicoding','Indonesia']))        # Output: Dicoding123Indonesia

print('Dicoding Indonesia !'.split())              # Output: ['Dicoding', 'Indonesia', '!']

teks_multiline = '''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''
print(teks_multiline.split('\n'))

# ====== 5. Mengganti Substring ======
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))  # Output: Ayo belajar Pemrograman di Dicoding

# ====== 6. Pengecekan Tipe Karakter ======
kata = 'DICODING'
print(kata.isupper())  # Output: True

kata = 'dicoding'
print(kata.islower())  # Output: True

kata = 'dicoding'
print(kata.isalpha())  # Output: True

kata = 'dicoding123'
print(kata.isalnum())  # Output: True

print('123'.isdecimal())     # Output: True
print('         '.isspace()) # Output: True
print('Dicoding Indonesia'.istitle())  # Output: True

# ====== 7. Formatting String ======
teks = 'Code'
print(teks.zfill(5))         # Output: 0Code

print('Dicoding'.rjust(20))     # Output:            Dicoding
print('Dicoding'.rjust(20, '!')) # Output: !!!!!!!!!!!!Dicoding

print('Dicoding'.ljust(20))     # Output: Dicoding           

print('Dicoding'.center(10, '-')) # Output: -Dicoding-

# ====== 8. String Literals & Escape Characters ======
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# Raw String
print(r'Dicoding\tIndonesia')  # Output: Dicoding\tIndonesia