""" 
Python Interpreter
Python termasuk bahasa pemrograman yang mudah dimengerti oleh manusia karena sintaksnya yang mudah dipahami. Tahukah Anda bahwa proses komputer menjalankan kode yang Anda bangun tidak sesederhana Anda memahaminya? 

Kode dari program Python yang Anda bangun akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan program compiler atau interpreter. Compiler merupakan program yang akan menerjemahkan bahasa pemrograman menjadi bahasa mesin sebelum dijalankan dan menghasilkan output. Ini artinya program yang Anda bangun secara keseluruhan akan diubah terlebih dahulu semuanya menjadi bahasa mesin. 

"""

# ============================================================
# PYTHON INTERPRETER & DASAR PENULISAN KODE
# ============================================================

# --- 1. COMPILER vs INTERPRETER ---
# Compiler  : menerjemahkan SELURUH kode ke bahasa mesin sebelum dijalankan
# Interpreter: menerjemahkan kode SATU PER SATU dan langsung menghasilkan output
# Python menggunakan INTERPRETER


# --- 2. BLOCK CODE ---
# Blok kode adalah potongan program yang dijalankan sebagai satu unit
# (fungsi, kelas, loop, dsb.)

# Contoh BENAR - indentasi 4 spasi
for i in range(10):
    print(i)  # Output: 0 sampai 9

# Contoh SALAH - tanpa indentasi → IndentationError
# for i in range(10):
# print(i)  # ❌ IndentationError: expected an indented block


# --- 3. INDENTASI ---
# Python WAJIB menggunakan indentasi (4 spasi) untuk menandai blok kode
# Indentasi menentukan awal dan akhir sebuah blok


# --- 4. CASE-SENSITIVE ---
# Python membedakan huruf besar dan kecil

teks = "Dicoding"    # variabel 'teks'
Teks = "Indonesia"   # variabel 'Teks' → BERBEDA dengan 'teks'

print(teks)   # Output: Dicoding
print(Teks)   # Output: Indonesia
# print(TEks) # ❌ NameError: name 'TEks' is not defined