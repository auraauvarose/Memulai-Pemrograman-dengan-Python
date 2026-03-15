# ============================================================
# RINGKASAN TIPE DATA PYTHON
# ============================================================


# ------------------------------------------------------------
# A. TIPE DATA PRIMITIF
# ------------------------------------------------------------

# 1. NUMBERS
# ----------
integer_val = 10          # int: bilangan bulat
float_val   = 3.14        # float: bilangan desimal
complex_val = 1 + 2j      # complex: bilangan kompleks

print("=== NUMBERS ===")
print(type(integer_val))  # <class 'int'>
print(type(float_val))    # <class 'float'>
print(type(complex_val))  # <class 'complex'>


# 2. BOOLEAN
# ----------
print("\n=== BOOLEAN ===")
is_raining = True
is_married = False
print(type(is_raining))   # <class 'bool'>

# Nilai yang dianggap False:
# None, False, 0, 0.0, 0j, "", (), [], {}, set(), range(0)


# 3. STRING
# ----------
print("\n=== STRING ===")
name = "Perseus Evans"
print(type(name))         # <class 'str'>

# Multi-line string
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu."""
print(multi_line)

# Indexing & Slicing
x = "Dicoding"
print(x)               # D
print(x[2:])              # coding

# String bersifat IMMUTABLE (tidak bisa diubah per karakter)
# x = 'F'  --> TypeError!

# Cara menampilkan string dengan variabel
print(f"Hello, nama saya {name}")            # f-string (direkomendasikan)
print("Nama saya %s" % name)                 # %-formatting
print("Nama saya {}".format(name))           # str.format()


# ------------------------------------------------------------
# B. TIPE DATA COLLECTION
# ------------------------------------------------------------

# 1. LIST — ordered, mutable, boleh duplikat
# ------------------------------------------
print("\n=== LIST ===")
my_list = ["laptop", "monitor", "mouse", "mousepad", "keyboard"]
print(type(my_list))      # <class 'list'>

# Indexing
print(my_list)         # laptop
print(my_list[-1])        # keyboard

# Slicing: list[start:stop:step]
print(my_list[0:4:2])     # ['laptop', 'mouse']
print(my_list[1:])        # dari indeks 1 hingga akhir
print(my_list[:3])        # dari awal hingga indeks 2

# Mengubah elemen (mutable)
my_list = "tablet"
print(my_list)


# 2. TUPLE — ordered, immutable
# ------------------------------
print("\n=== TUPLE ===")
my_tuple = (5, "program", 1 + 3j)
print(type(my_tuple))     # <class 'tuple'>
print(my_tuple)        # program
print(my_tuple[0:3])      # seluruh elemen

# Tuple bersifat IMMUTABLE
# my_tuple = 'Dicoding'  --> TypeError!


# 3. SET — unordered, unik, tanpa duplikat
# -----------------------------------------
print("\n=== SET ===")
my_set = {1, 2, 7, 2, 3, 13, 3}
print(my_set)             # {1, 2, 3, 7, 13} — duplikat dihapus
print(type(my_set))       # <class 'set'>

# Set tidak mendukung indexing!
# print(my_set)  --> TypeError!

# Operasi himpunan
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1.union(set2))              # {1,2,3,4,5,6,7,8}
print("Intersection:", set1.intersection(set2))# {4, 5}


# 4. DICTIONARY — key-value pairs, unordered
# -------------------------------------------
print("\n=== DICTIONARY ===")
person = {"name": "Perseus Evans", "age": 20, "isMarried": False}
print(type(person))       # <class 'dict'>

# Akses nilai via key
print(person["name"])     # Perseus Evans

# Tambah data
person["job"] = "Web Developer"
print(person)

# Ubah data
person["name"] = "Dicoding"
print(person)

# Hapus data
del person["isMarried"]
print(person)


# ------------------------------------------------------------
# C. KONVERSI TIPE DATA
# ------------------------------------------------------------
print("\n=== KONVERSI TIPE DATA ===")

# Integer <-> Float
print(float(5))           # 5.0
print(int(5.6))           # 5 (desimal dipotong, bukan dibulatkan)

# Dari/ke String
print(int("25"))          # 25
print(str(25))            # '25'
print(float("25"))        # 25.0
# print(int("1p"))        # ValueError!

# Konversi antar collection
print(set([1, 2, 3]))     # {1, 2, 3}
print(tuple({5, 6, 7}))   # (5, 6, 7)
print(list("hello"))      # ['h','e','l','l','o']

# Konversi ke Dictionary
print(dict([[1, 2], [3, 4]]))   # {1: 2, 3: 4}
print(dict([(3, 26), (4, 44)])) # {3: 26, 4: 44}


# ------------------------------------------------------------
# RINGKASAN SIFAT TIPE DATA
# ------------------------------------------------------------
# | Tipe Data  | Ordered | Mutable | Duplikat | Akses      |
# |------------|---------|---------|----------|------------|
# | int/float  |    -    |   No    |    -     | nilai      |
# | bool       |    -    |   No    |    -     | nilai      |
# | string     |   Yes   |   No    |   Yes    | index      |
# | list       |   Yes   |   Yes   |   Yes    | index      |
# | tuple      |   Yes   |   No    |   Yes    | index      |
# | set        |   No    |   Yes   |   No     | -          |
# | dictionary |   No    |   Yes   |  No(key) | key        |
# ------------------------------------------------------------