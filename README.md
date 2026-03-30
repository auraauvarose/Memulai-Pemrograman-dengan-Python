# Memulai Pemrograman dengan Python

Repositori ini berisi kumpulan materi, kode contoh, kuis, dan tugas untuk belajar pemrograman Python dari dasar hingga konsep control flow.

## Struktur Proyek

```
.
├── 01. Berkenalan dengan python/
├── 02. Berinteraksi dengan Data/
├── 03. Ekspresi/
├── 04. Aksi Sekuensial/
├── 05. control_flow/
├── 06. Array dan Pemrosesannya/    (segera)
└── Materi kuliah/
```

## Daftar Materi

### 01. Berkenalan dengan Python

Pengenalan dasar-dasar Python: menjalankan kode pertama, variabel, assignment, input/output, dan komentar.

| File | Deskripsi |
|------|-----------|
| [`main.py`](01.%20Berkenalan%20dengan%20python/main.py) | Program "Hello World", `print()`, komentar, multiple assignment |
| [`variable_dan_assignment.py`](01.%20Berkenalan%20dengan%20python/variable_dan_assignment.py) | Konsep variabel dan assignment |
| [`input_output_dan_komentar.py`](01.%20Berkenalan%20dengan%20python/input_output_dan_komentar.py) | `input()`, `print()`, dan komentar |

**Topik:** Pengenalan Python, Menjalankan Kode, Variabel & Assignment, Input/Output & Komentar

---

### 02. Berinteraksi dengan Data

Mempelajari tipe data, pengetikan data, transformasi, dan operasi pada koleksi (list, set, string).

| File | Deskripsi |
|------|-----------|
| [`data_typing.py`](02.%20Berinteraksi%20dengan%20Data/data_typing.py) | Pengecekan tipe data dengan `type()` |
| [`tipe_data.py`](02.%20Berinteraksi%20dengan%20Data/tipe_data.py) | Referensi lengkap tipe data: int, float, str, list, tuple, set, dict |
| [`transformasi.py`](02.%20Berinteraksi%20dengan%20Data/transformasi.py) | Metode transformasi string: `upper()`, `split()`, `replace()`, dll. |
| [`operasi.py`](02.%20Berinteraksi%20dengan%20Data/operasi.py) | Operasi koleksi: `len()`, `min()`, `max()`, `sort()`, membership check |

**Topik:** Abstraksi Data, Data Typing, Tipe Data, Transformasi Angka/Karakter/String, Operasi List/Set/String

---

### 03. Ekspresi

Memahami ekspresi, jenis-jenis ekspresi, dan operator (aritmatika, relasional, logika, assignment).

| File | Deskripsi |
|------|-----------|
| [`ekspresi.py`](03.%20Ekspresi/ekspresi.py) | Contoh ekspresi dasar: pengurangan, penggabungan list |
| [`jenis2_operator.py`](03.%20Ekspresi/jenis2_operator.py) | Referensi operator: aritmatika, relasional, logika, assignment |
| [`kuis coding/predikat_nilai.py`](03.%20Ekspresi/kuis%20coding/predikat_nilai.py) | Kuis: Predikat nilai ujian (if-elif-else) |
| [`kuis coding/main.py`](03.%20Ekspresi/kuis%20coding/main.py) | Kuis: Kalkulator diskon belanja |
| [`kuis coding/akses_lab.py`](03.%20Ekspresi/kuis%20coding/akses_lab.py) | Kuis: Pengecekan akses lab dengan operator `and` |

**Topik:** Pengertian Ekspresi, Jenis-Jenis Ekspresi & Operator

---

### 04. Aksi Sekuensial

Memahami cara kerja Python interpreter, indentation, case-sensitivity, dan teknik one-liner.

| File | Deskripsi |
|------|-----------|
| [`python_interpreter.py`](04.%20Aksi%20Sekuensial/python_interpreter.py) | Compiler vs Interpreter, aturan indentasi, case-sensitivity |
| [`one_liner.py`](04.%20Aksi%20Sekuensial/one_liner.py) | Teknik swap variabel one-liner: `x, y = y, x` |

**Topik:** Pengenalan Aksi Sekuensial, Python Interpreter, One-liner

---

### 05. Control Flow

Percabangan (if/elif/else, ternary), perulangan (for, while), kontrol perulangan (break, continue), dan error handling.

| File | Deskripsi |
|------|-----------|
| [`percabangan_dan_ternary_operators.py`](05.%20control_flow/percabangan_dan_ternary_operators.py) | if-else, if-elif-else, ternary operator |
| [`perulangan.py`](05.%20control_flow/perulangan.py) | for loop, range(), while loop, nested loop |
| [`kontrol_perulangan.py`](05.%20control_flow/kontrol_perulangan.py) | `break`, `continue`, `else` setelah `for` |
| [`kuis coding/warung_digital.py`](05.%20control_flow/kuis%20coding/warung_digital.py) | Kuis: Sistem pemesanan warung digital |
| [`kuis coding/callculator.py`](05.%20control_flow/kuis%20coding/callculator.py) | Kuis: Kalkulator sederhana |

**Topik:** Percabangan & Ternary Operators, Perulangan, Error Handling

---

### 06. Array dan Pemrosesannya

> **Status:** Belum tersedia.

---

### Materi Kuliah

Materi tambahan dan tugas dari perkuliahan.

| File | Deskripsi |
|------|-----------|
| [`if_else.py`](Materi%20kuliah/if_else.py) | Contoh if-else: harga tiket, perbandingan nilai, grade |
| [`while.py`](Materi%20kuliah/while.py) | Contoh while loop dan `continue` |
| [`perulangan.py`](Materi%20kuliah/perulangan.py) | Contoh for loop, `enumerate()`, `range()` |
| [`Tugas/tugas_if_else.py`](Materi%20kuliah/Tugas/tugas_if_else.py) | Tugas: Pengklasifikasi bilangan positif/negatif/nol |
| [`Tugas/tugas_solo.py`](Materi%20kuliah/Tugas/tugas_solo.py) | Tugas: Simulasi pertumbuhan populasi Solo vs Yogyakarta |
| [`Tugas/tugas_perulangan.py`](Materi%20kuliah/Tugas/tugas_perulangan.py) | Tugas: Menjumlahkan input hingga 0 |

---

## Prasyarat

- **Python 3.x** - [Download Python](https://www.python.org/downloads/)
- Text editor atau IDE (VS Code, PyCharm, dll.)

## Cara Menjalankan

1. Clone repositori ini:
   ```bash
   git clone <url-repositori>
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd "Memulai Pemrograman dengan Python"
   ```

3. Jalankan file Python yang diinginkan:
   ```bash
   python "01. Berkenalan dengan python/main.py"
   ```

   Atau gunakan `python3` jika `python` tidak ditemukan:
   ```bash
   python3 "01. Berkenalan dengan python/main.py"
   ```

## Alur Belajar

Disarankan mengikuti materi secara berurutan:

```
01. Berkenalan dengan Python    (Dasar: print, variabel, input)
        │
        ▼
02. Berinteraksi dengan Data    (Tipe data, operasi koleksi)
        │
        ▼
03. Ekspresi                    (Operator, ekspresi)
        │
        ▼
04. Aksi Sekuensial             (Interpreter, indentasi)
        │
        ▼
05. Control Flow                (if/elif/else, for, while)
        │
        ▼
06. Array dan Pemrosesannya     (Akan datang)
```

## Referensi

- [Dokumentasi Python Resmi](https://docs.python.org/3/)
- [Python Tutorial - W3Schools](https://www.w3schools.com/python/)
- [Belajar Python - Dicoding](https://www.dicoding.com/academies)
