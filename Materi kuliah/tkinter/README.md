# 📚 Panduan Belajar MariaDB / MySQL
> Panduan lengkap belajar database MariaDB dari nol — mulai dari instalasi, operasi dasar, hingga query lanjutan.

---

## 📋 Daftar Isi

1. [Menjalankan MariaDB](#1-menjalankan-mariadb)
2. [Menjalankan phpMyAdmin](#2-menjalankan-phpmyadmin)
3. [Operasi Database](#3-operasi-database)
4. [Membuat Tabel](#4-membuat-tabel)
5. [INSERT — Menambah Data](#5-insert--menambah-data)
6. [SELECT — Menampilkan Data](#6-select--menampilkan-data)
7. [WHERE — Filter Data](#7-where--filter-data)
8. [UPDATE — Mengubah Data](#8-update--mengubah-data)
9. [DELETE — Menghapus Data](#9-delete--menghapus-data)
10. [ORDER BY & LIMIT](#10-order-by--limit)
11. [Fungsi Agregat](#11-fungsi-agregat)
12. [GROUP BY & HAVING](#12-group-by--having)
13. [LIKE & BETWEEN & IN](#13-like--between--in)
14. [JOIN — Relasi Antar Tabel](#14-join--relasi-antar-tabel)
15. [Tipe Data MySQL](#15-tipe-data-mysql)
16. [Constraint & Primary Key](#16-constraint--primary-key)
17. [ALTER TABLE — Mengubah Struktur Tabel](#17-alter-table--mengubah-struktur-tabel)
18. [Tips & Perintah Penting](#18-tips--perintah-penting)
19. [Contoh Studi Kasus Lengkap](#19-contoh-studi-kasus-lengkap)

---

## 1. Menjalankan MariaDB

### Start Service MariaDB
```bash
# Jalankan MariaDB
sudo systemctl start mariadb

# Hentikan MariaDB
sudo systemctl stop mariadb

# Restart MariaDB
sudo systemctl restart mariadb

# Cek status MariaDB
sudo systemctl status mariadb

# Aktifkan MariaDB saat boot (opsional)
sudo systemctl enable mariadb
```

### Login ke MariaDB via Terminal
```bash
# Login sebagai root (dengan password)
sudo mysql -u root -p

# Login sebagai root (tanpa password)
sudo mysql -u root

# Login dengan user tertentu
mysql -u nama_user -p nama_database
```

Setelah login, prompt akan berubah menjadi:
```
MariaDB [(none)]>
```

### Keluar dari MariaDB
```sql
EXIT;
-- atau
QUIT;
```

---

## 2. Menjalankan phpMyAdmin

### Start Apache (Web Server)
```bash
# Jalankan Apache
sudo systemctl start httpd

# Hentikan Apache
sudo systemctl stop httpd

# Restart Apache
sudo systemctl restart httpd
```

### Akses phpMyAdmin
1. Buka browser
2. Ketik: `http://localhost/phpmyadmin`
3. Login dengan:
   - **Username:** `root`
   - **Password:** password MariaDB kamu

> 💡 **Tips:** phpMyAdmin adalah antarmuka grafis untuk mengelola database tanpa harus mengetik query manual.

---

## 3. Operasi Database

### Melihat Semua Database
```sql
SHOW DATABASES;
```
Output:
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

### Membuat Database Baru
```sql
-- Buat database biasa
CREATE DATABASE nama_database;

-- Buat database dengan charset UTF-8 (direkomendasikan)
CREATE DATABASE nama_database 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Buat database hanya jika belum ada
CREATE DATABASE IF NOT EXISTS nama_database;
```

### Memilih/Menggunakan Database
```sql
USE nama_database;
```

### Menghapus Database
```sql
-- Hapus database (HATI-HATI! Tidak bisa dibatalkan)
DROP DATABASE nama_database;

-- Hapus database hanya jika ada
DROP DATABASE IF EXISTS nama_database;
```

### Melihat Database yang Sedang Aktif
```sql
SELECT DATABASE();
```

---

## 4. Membuat Tabel

### Sintaks Dasar CREATE TABLE
```sql
CREATE TABLE nama_tabel (
    kolom1 tipe_data constraint,
    kolom2 tipe_data constraint,
    ...
);
```

### Contoh Membuat Tabel Mahasiswa
```sql
CREATE TABLE mahasiswa (
    nim        VARCHAR(10)  PRIMARY KEY,
    nama       VARCHAR(100) NOT NULL,
    jurusan    VARCHAR(50)  NOT NULL,
    angkatan   YEAR         NOT NULL,
    ipk        DECIMAL(3,2) DEFAULT 0.00,
    email      VARCHAR(100) UNIQUE,
    created_at TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);
```

### Contoh Membuat Tabel Produk
```sql
CREATE TABLE produk (
    id_produk    INT          AUTO_INCREMENT PRIMARY KEY,
    nama_produk  VARCHAR(100) NOT NULL,
    harga        DECIMAL(10,2) NOT NULL,
    stok         INT          DEFAULT 0,
    kategori     VARCHAR(50),
    deskripsi    TEXT,
    created_at   TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);
```

### Melihat Struktur Tabel
```sql
-- Tampilkan struktur tabel
DESCRIBE mahasiswa;
-- atau
DESC mahasiswa;

-- Tampilkan query CREATE TABLE
SHOW CREATE TABLE mahasiswa;
```

### Melihat Semua Tabel di Database
```sql
SHOW TABLES;
```

---

## 5. INSERT — Menambah Data

### Insert Satu Baris Data
```sql
-- Insert dengan menyebut nama kolom (DIREKOMENDASIKAN)
INSERT INTO mahasiswa (nim, nama, jurusan, angkatan, ipk, email)
VALUES ('2024001', 'Aura Rose', 'Informatika', 2024, 3.85, 'aura@email.com');

-- Insert tanpa nama kolom (harus urut sesuai kolom tabel)
INSERT INTO mahasiswa
VALUES ('2024002', 'Budi Santoso', 'Sistem Informasi', 2024, 3.50, 'budi@email.com', NOW());
```

### Insert Banyak Baris Sekaligus
```sql
INSERT INTO mahasiswa (nim, nama, jurusan, angkatan, ipk) VALUES
('2024003', 'Citra Dewi',    'Informatika',      2024, 3.70),
('2024004', 'Deni Kurnia',   'Teknik Komputer',  2024, 3.20),
('2024005', 'Eka Putri',     'Informatika',      2023, 3.90),
('2024006', 'Fajar Hidayat', 'Sistem Informasi', 2023, 3.15);
```

### Insert dengan SELECT (Menyalin Data dari Tabel Lain)
```sql
-- Salin data dari tabel lama ke tabel baru
INSERT INTO mahasiswa_backup (nim, nama, jurusan)
SELECT nim, nama, jurusan FROM mahasiswa;
```

> ⚠️ **Penting:** Jika kolom `id` menggunakan `AUTO_INCREMENT`, tidak perlu diisi — akan otomatis bertambah.

---

## 6. SELECT — Menampilkan Data

### Menampilkan Semua Data
```sql
-- Tampilkan semua kolom
SELECT * FROM mahasiswa;

-- Tampilkan kolom tertentu saja
SELECT nim, nama, ipk FROM mahasiswa;
```

### Memberi Alias pada Kolom
```sql
SELECT 
    nim        AS 'Nomor Induk',
    nama       AS 'Nama Mahasiswa',
    jurusan    AS 'Program Studi',
    ipk        AS 'IPK'
FROM mahasiswa;
```

### Menghilangkan Duplikasi (DISTINCT)
```sql
-- Tampilkan jurusan yang unik (tidak duplikat)
SELECT DISTINCT jurusan FROM mahasiswa;
```

### Menampilkan Data dengan Ekspresi
```sql
-- Hitung nilai dengan rumus
SELECT 
    nama,
    harga,
    harga * 0.1 AS 'Diskon 10%',
    harga - (harga * 0.1) AS 'Harga Setelah Diskon'
FROM produk;
```

---

## 7. WHERE — Filter Data

### Operator Perbandingan
```sql
-- Sama dengan
SELECT * FROM mahasiswa WHERE jurusan = 'Informatika';

-- Tidak sama dengan
SELECT * FROM mahasiswa WHERE jurusan != 'Informatika';
-- atau
SELECT * FROM mahasiswa WHERE jurusan <> 'Informatika';

-- Lebih besar dari
SELECT * FROM mahasiswa WHERE ipk > 3.5;

-- Lebih kecil dari
SELECT * FROM mahasiswa WHERE ipk < 3.0;

-- Lebih besar atau sama dengan
SELECT * FROM mahasiswa WHERE ipk >= 3.5;

-- Lebih kecil atau sama dengan
SELECT * FROM mahasiswa WHERE angkatan <= 2023;
```

### Operator Logika AND, OR, NOT
```sql
-- AND — kedua kondisi harus terpenuhi
SELECT * FROM mahasiswa 
WHERE jurusan = 'Informatika' AND ipk >= 3.5;

-- OR — salah satu kondisi terpenuhi
SELECT * FROM mahasiswa 
WHERE jurusan = 'Informatika' OR jurusan = 'Sistem Informasi';

-- NOT — kebalikan dari kondisi
SELECT * FROM mahasiswa 
WHERE NOT jurusan = 'Teknik Komputer';

-- Kombinasi AND dan OR
SELECT * FROM mahasiswa 
WHERE (jurusan = 'Informatika' OR jurusan = 'Sistem Informasi') 
AND ipk >= 3.0;
```

### IS NULL / IS NOT NULL
```sql
-- Data yang tidak memiliki email
SELECT * FROM mahasiswa WHERE email IS NULL;

-- Data yang memiliki email
SELECT * FROM mahasiswa WHERE email IS NOT NULL;
```

---

## 8. UPDATE — Mengubah Data

### Sintaks Dasar UPDATE
```sql
UPDATE nama_tabel 
SET kolom1 = nilai_baru1, kolom2 = nilai_baru2
WHERE kondisi;
```

### Contoh UPDATE
```sql
-- Update satu kolom
UPDATE mahasiswa 
SET ipk = 3.95 
WHERE nim = '2024001';

-- Update banyak kolom sekaligus
UPDATE mahasiswa 
SET jurusan = 'Teknik Informatika', ipk = 3.80
WHERE nim = '2024002';

-- Update dengan kondisi angkatan
UPDATE mahasiswa 
SET status = 'Aktif'
WHERE angkatan = 2024;

-- Update menggunakan nilai kolom yang ada
UPDATE produk 
SET stok = stok + 10
WHERE id_produk = 1;

-- Update dengan kalkulasi harga
UPDATE produk 
SET harga = harga * 1.1  -- Naikkan harga 10%
WHERE kategori = 'Elektronik';
```

> ⚠️ **PERINGATAN:** Selalu gunakan `WHERE` saat `UPDATE`! Tanpa `WHERE`, **semua baris** akan diubah.

```sql
-- BERBAHAYA! Semua IPK akan jadi 0
UPDATE mahasiswa SET ipk = 0;

-- AMAN — Hanya mengubah IPK mahasiswa tertentu
UPDATE mahasiswa SET ipk = 0 WHERE nim = '2024001';
```

---

## 9. DELETE — Menghapus Data

### Sintaks Dasar DELETE
```sql
DELETE FROM nama_tabel WHERE kondisi;
```

### Contoh DELETE
```sql
-- Hapus satu data berdasarkan ID
DELETE FROM mahasiswa WHERE nim = '2024006';

-- Hapus data berdasarkan kondisi
DELETE FROM produk WHERE stok = 0;

-- Hapus data dengan kondisi ganda
DELETE FROM mahasiswa 
WHERE jurusan = 'Teknik Komputer' AND angkatan < 2020;
```

### Menghapus Semua Data di Tabel
```sql
-- DELETE tanpa WHERE (menghapus semua baris, tabel tetap ada)
DELETE FROM mahasiswa;

-- TRUNCATE (lebih cepat, reset AUTO_INCREMENT)
TRUNCATE TABLE mahasiswa;
```

### Menghapus Tabel
```sql
-- Hapus tabel beserta semua datanya
DROP TABLE nama_tabel;

-- Hapus tabel hanya jika ada
DROP TABLE IF EXISTS nama_tabel;
```

> ⚠️ **PERINGATAN:** Selalu gunakan `WHERE` saat `DELETE`! Tanpa `WHERE`, **semua data** akan terhapus permanen.

---

## 10. ORDER BY & LIMIT

### ORDER BY — Mengurutkan Data
```sql
-- Urut A-Z (ascending, default)
SELECT * FROM mahasiswa ORDER BY nama ASC;

-- Urut Z-A (descending)
SELECT * FROM mahasiswa ORDER BY nama DESC;

-- Urut berdasarkan IPK tertinggi
SELECT * FROM mahasiswa ORDER BY ipk DESC;

-- Urut berdasarkan beberapa kolom
SELECT * FROM mahasiswa 
ORDER BY jurusan ASC, ipk DESC;
```

### LIMIT — Membatasi Jumlah Data
```sql
-- Tampilkan 5 data saja
SELECT * FROM mahasiswa LIMIT 5;

-- Tampilkan 5 data mulai dari baris ke-11 (untuk pagination)
SELECT * FROM mahasiswa LIMIT 10, 5;
-- atau
SELECT * FROM mahasiswa LIMIT 5 OFFSET 10;
```

### Kombinasi ORDER BY + LIMIT
```sql
-- Tampilkan 3 mahasiswa dengan IPK tertinggi
SELECT nama, jurusan, ipk 
FROM mahasiswa 
ORDER BY ipk DESC 
LIMIT 3;

-- Tampilkan produk termurah
SELECT nama_produk, harga 
FROM produk 
ORDER BY harga ASC 
LIMIT 5;
```

---

## 11. Fungsi Agregat

Fungsi agregat digunakan untuk menghitung nilai dari sekumpulan data.

```sql
-- COUNT — Menghitung jumlah baris
SELECT COUNT(*) AS total_mahasiswa FROM mahasiswa;
SELECT COUNT(email) AS yang_punya_email FROM mahasiswa;  -- Tidak menghitung NULL

-- SUM — Menjumlahkan nilai
SELECT SUM(stok) AS total_stok FROM produk;
SELECT SUM(harga * stok) AS total_nilai_inventori FROM produk;

-- AVG — Rata-rata
SELECT AVG(ipk) AS rata_rata_ipk FROM mahasiswa;
SELECT ROUND(AVG(ipk), 2) AS rata_rata_ipk FROM mahasiswa;  -- 2 desimal

-- MAX — Nilai terbesar
SELECT MAX(ipk) AS ipk_tertinggi FROM mahasiswa;
SELECT MAX(harga) AS harga_termahal FROM produk;

-- MIN — Nilai terkecil
SELECT MIN(ipk) AS ipk_terendah FROM mahasiswa;
SELECT MIN(harga) AS harga_termurah FROM produk;
```

### Kombinasi Fungsi Agregat
```sql
SELECT 
    COUNT(*)     AS total_mahasiswa,
    ROUND(AVG(ipk), 2) AS rata_rata_ipk,
    MAX(ipk)     AS ipk_tertinggi,
    MIN(ipk)     AS ipk_terendah
FROM mahasiswa;
```

---

## 12. GROUP BY & HAVING

### GROUP BY — Mengelompokkan Data
```sql
-- Hitung jumlah mahasiswa per jurusan
SELECT jurusan, COUNT(*) AS jumlah_mahasiswa
FROM mahasiswa
GROUP BY jurusan;

-- Rata-rata IPK per jurusan
SELECT jurusan, ROUND(AVG(ipk), 2) AS rata_ipk
FROM mahasiswa
GROUP BY jurusan;

-- Total stok per kategori produk
SELECT kategori, SUM(stok) AS total_stok, COUNT(*) AS jumlah_produk
FROM produk
GROUP BY kategori;
```

### HAVING — Filter Setelah GROUP BY
> `HAVING` seperti `WHERE` tapi untuk hasil GROUP BY

```sql
-- Tampilkan jurusan yang memiliki lebih dari 2 mahasiswa
SELECT jurusan, COUNT(*) AS jumlah
FROM mahasiswa
GROUP BY jurusan
HAVING jumlah > 2;

-- Tampilkan jurusan dengan rata-rata IPK di atas 3.5
SELECT jurusan, ROUND(AVG(ipk), 2) AS rata_ipk
FROM mahasiswa
GROUP BY jurusan
HAVING rata_ipk >= 3.5;
```

> 💡 **Perbedaan WHERE vs HAVING:**
> - `WHERE` — Filter **sebelum** pengelompokan
> - `HAVING` — Filter **setelah** pengelompokan

```sql
-- WHERE dulu (filter angkatan 2024), baru GROUP BY, baru HAVING
SELECT jurusan, COUNT(*) AS jumlah, AVG(ipk) AS rata_ipk
FROM mahasiswa
WHERE angkatan = 2024          -- Filter dulu
GROUP BY jurusan               -- Lalu kelompokkan
HAVING AVG(ipk) >= 3.5;       -- Lalu filter hasil group
```

---

## 13. LIKE, BETWEEN & IN

### LIKE — Pencarian Pola Teks
```sql
-- % = cocok dengan nol atau lebih karakter
-- _ = cocok dengan tepat satu karakter

-- Nama yang dimulai dengan 'A'
SELECT * FROM mahasiswa WHERE nama LIKE 'A%';

-- Nama yang diakhiri dengan 'i'
SELECT * FROM mahasiswa WHERE nama LIKE '%i';

-- Nama yang mengandung 'aura' (di mana saja)
SELECT * FROM mahasiswa WHERE nama LIKE '%aura%';

-- Nama dengan 4 karakter diawali 'B'
SELECT * FROM mahasiswa WHERE nama LIKE 'B___';

-- Case insensitive (tidak peduli huruf besar/kecil)
SELECT * FROM mahasiswa WHERE LOWER(nama) LIKE '%rose%';
```

### BETWEEN — Rentang Nilai
```sql
-- IPK antara 3.0 dan 3.5
SELECT * FROM mahasiswa WHERE ipk BETWEEN 3.0 AND 3.5;

-- Angkatan antara 2022 dan 2024
SELECT * FROM mahasiswa WHERE angkatan BETWEEN 2022 AND 2024;

-- Harga antara 100.000 dan 500.000
SELECT * FROM produk WHERE harga BETWEEN 100000 AND 500000;

-- NOT BETWEEN — di luar rentang
SELECT * FROM produk WHERE harga NOT BETWEEN 100000 AND 500000;
```

### IN — Memilih dari Daftar Nilai
```sql
-- Mahasiswa dari jurusan tertentu
SELECT * FROM mahasiswa 
WHERE jurusan IN ('Informatika', 'Sistem Informasi');

-- Produk dengan kategori tertentu
SELECT * FROM produk 
WHERE kategori IN ('Elektronik', 'Aksesori', 'Furniture');

-- NOT IN — bukan dari daftar tersebut
SELECT * FROM mahasiswa 
WHERE jurusan NOT IN ('Teknik Komputer');
```

---

## 14. JOIN — Relasi Antar Tabel

JOIN digunakan untuk menggabungkan data dari dua tabel atau lebih berdasarkan kolom yang berelasi.

### Contoh Tabel untuk JOIN
```sql
-- Tabel jurusan
CREATE TABLE jurusan (
    id_jurusan   INT         AUTO_INCREMENT PRIMARY KEY,
    nama_jurusan VARCHAR(50) NOT NULL,
    fakultas     VARCHAR(50) NOT NULL
);

INSERT INTO jurusan (nama_jurusan, fakultas) VALUES
('Informatika',      'Teknik'),
('Sistem Informasi', 'Teknik'),
('Teknik Komputer',  'Teknik');

-- Tabel mahasiswa dengan foreign key
CREATE TABLE mahasiswa (
    nim        VARCHAR(10) PRIMARY KEY,
    nama       VARCHAR(100) NOT NULL,
    id_jurusan INT,
    angkatan   YEAR,
    ipk        DECIMAL(3,2)
);
```

### INNER JOIN — Data yang Ada di Kedua Tabel
```sql
-- Tampilkan mahasiswa beserta nama jurusannya
SELECT 
    m.nim,
    m.nama,
    j.nama_jurusan,
    j.fakultas,
    m.ipk
FROM mahasiswa m
INNER JOIN jurusan j ON m.id_jurusan = j.id_jurusan;
```

### LEFT JOIN — Semua Data dari Tabel Kiri
```sql
-- Tampilkan semua mahasiswa, termasuk yang tidak punya jurusan
SELECT 
    m.nim,
    m.nama,
    j.nama_jurusan
FROM mahasiswa m
LEFT JOIN jurusan j ON m.id_jurusan = j.id_jurusan;
```

### RIGHT JOIN — Semua Data dari Tabel Kanan
```sql
-- Tampilkan semua jurusan, termasuk yang tidak ada mahasiswanya
SELECT 
    j.nama_jurusan,
    m.nim,
    m.nama
FROM mahasiswa m
RIGHT JOIN jurusan j ON m.id_jurusan = j.id_jurusan;
```

### JOIN 3 Tabel
```sql
-- Contoh: mahasiswa - nilai - mata_kuliah
SELECT 
    m.nama,
    mk.nama_matkul,
    n.nilai
FROM mahasiswa m
JOIN nilai n ON m.nim = n.nim
JOIN mata_kuliah mk ON n.id_matkul = mk.id_matkul
ORDER BY m.nama;
```

---

## 15. Tipe Data MySQL

### Tipe Data Angka
| Tipe | Ukuran | Keterangan |
|------|--------|------------|
| `TINYINT` | 1 byte | -128 sampai 127 |
| `INT` | 4 byte | -2 juta sampai 2 juta |
| `BIGINT` | 8 byte | Angka sangat besar |
| `FLOAT` | 4 byte | Bilangan desimal (presisi rendah) |
| `DOUBLE` | 8 byte | Bilangan desimal (presisi tinggi) |
| `DECIMAL(M,D)` | Variabel | Desimal tepat, M=total digit, D=desimal |

### Tipe Data Teks
| Tipe | Ukuran | Keterangan |
|------|--------|------------|
| `CHAR(N)` | N byte | Panjang tetap, max 255 |
| `VARCHAR(N)` | 1-N byte | Panjang variabel, max 65535 |
| `TEXT` | Max 64KB | Teks panjang |
| `LONGTEXT` | Max 4GB | Teks sangat panjang |

### Tipe Data Tanggal & Waktu
| Tipe | Format | Keterangan |
|------|--------|------------|
| `DATE` | YYYY-MM-DD | Tanggal saja |
| `TIME` | HH:MM:SS | Waktu saja |
| `DATETIME` | YYYY-MM-DD HH:MM:SS | Tanggal dan waktu |
| `TIMESTAMP` | YYYY-MM-DD HH:MM:SS | Seperti DATETIME, auto update |
| `YEAR` | YYYY | Tahun saja |

---

## 16. Constraint & Primary Key

### PRIMARY KEY
```sql
-- Single primary key
CREATE TABLE produk (
    id_produk INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(100)
);

-- Composite primary key (lebih dari satu kolom)
CREATE TABLE nilai (
    nim       VARCHAR(10),
    id_matkul INT,
    nilai     DECIMAL(5,2),
    PRIMARY KEY (nim, id_matkul)
);
```

### FOREIGN KEY
```sql
CREATE TABLE mahasiswa (
    nim        VARCHAR(10) PRIMARY KEY,
    nama       VARCHAR(100),
    id_jurusan INT,
    FOREIGN KEY (id_jurusan) REFERENCES jurusan(id_jurusan)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

### Constraint Lainnya
```sql
CREATE TABLE pengguna (
    id       INT          AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50)  NOT NULL UNIQUE,     -- Tidak boleh kosong & unik
    email    VARCHAR(100) UNIQUE,              -- Harus unik
    umur     INT          CHECK (umur >= 17),  -- Harus >= 17
    status   VARCHAR(10)  DEFAULT 'Aktif'      -- Nilai default
);
```

---

## 17. ALTER TABLE — Mengubah Struktur Tabel

```sql
-- Tambah kolom baru
ALTER TABLE mahasiswa ADD COLUMN no_telepon VARCHAR(15);

-- Tambah kolom di posisi tertentu
ALTER TABLE mahasiswa ADD COLUMN alamat TEXT AFTER nama;

-- Ubah tipe data kolom
ALTER TABLE mahasiswa MODIFY COLUMN ipk DECIMAL(4,2);

-- Ganti nama kolom
ALTER TABLE mahasiswa CHANGE COLUMN no_telepon telepon VARCHAR(15);

-- Hapus kolom
ALTER TABLE mahasiswa DROP COLUMN alamat;

-- Ganti nama tabel
ALTER TABLE mahasiswa RENAME TO data_mahasiswa;

-- Tambah index
ALTER TABLE mahasiswa ADD INDEX idx_nama (nama);
```

---

## 18. Tips & Perintah Penting

### Perintah Informasi
```sql
-- Database yang sedang aktif
SELECT DATABASE();

-- Versi MariaDB
SELECT VERSION();

-- Tanggal & waktu sekarang
SELECT NOW();
SELECT CURDATE();
SELECT CURTIME();

-- Tampilkan semua database
SHOW DATABASES;

-- Tampilkan semua tabel
SHOW TABLES;

-- Tampilkan struktur tabel
DESCRIBE nama_tabel;

-- Tampilkan query CREATE TABLE
SHOW CREATE TABLE nama_tabel;
```

### Fungsi String Berguna
```sql
-- Uppercase & Lowercase
SELECT UPPER('hello');      -- HELLO
SELECT LOWER('HELLO');      -- hello

-- Panjang string
SELECT LENGTH('Informatika');  -- 11

-- Gabung string
SELECT CONCAT(nama, ' - ', jurusan) AS info FROM mahasiswa;

-- Potong string
SELECT SUBSTRING('Informatika', 1, 5);  -- Infor

-- Hapus spasi
SELECT TRIM('  hello  ');  -- hello
```

### Fungsi Angka Berguna
```sql
-- Pembulatan
SELECT ROUND(3.567, 2);   -- 3.57
SELECT CEIL(3.2);          -- 4 (ke atas)
SELECT FLOOR(3.9);         -- 3 (ke bawah)

-- Nilai absolut
SELECT ABS(-5);            -- 5

-- Modulo (sisa bagi)
SELECT MOD(10, 3);         -- 1
```

### Backup & Restore Database
```bash
# Backup database
mysqldump -u root -p nama_database > backup.sql

# Backup semua database
mysqldump -u root -p --all-databases > semua_backup.sql

# Restore database
mysql -u root -p nama_database < backup.sql
```

---

## 19. Contoh Studi Kasus Lengkap

### Studi Kasus: Sistem Perpustakaan

```sql
-- Buat database
CREATE DATABASE perpustakaan;
USE perpustakaan;

-- Tabel anggota
CREATE TABLE anggota (
    id_anggota  INT         AUTO_INCREMENT PRIMARY KEY,
    nama        VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE,
    telepon     VARCHAR(15),
    tgl_daftar  DATE         DEFAULT (CURRENT_DATE)
);

-- Tabel buku
CREATE TABLE buku (
    id_buku     INT         AUTO_INCREMENT PRIMARY KEY,
    judul       VARCHAR(200) NOT NULL,
    pengarang   VARCHAR(100) NOT NULL,
    penerbit    VARCHAR(100),
    tahun_terbit YEAR,
    stok        INT         DEFAULT 1,
    kategori    VARCHAR(50)
);

-- Tabel peminjaman
CREATE TABLE peminjaman (
    id_pinjam   INT  AUTO_INCREMENT PRIMARY KEY,
    id_anggota  INT  NOT NULL,
    id_buku     INT  NOT NULL,
    tgl_pinjam  DATE DEFAULT (CURRENT_DATE),
    tgl_kembali DATE,
    status      VARCHAR(20) DEFAULT 'Dipinjam',
    FOREIGN KEY (id_anggota) REFERENCES anggota(id_anggota),
    FOREIGN KEY (id_buku) REFERENCES buku(id_buku)
);

-- Insert data anggota
INSERT INTO anggota (nama, email, telepon) VALUES
('Aura Rose',    'aura@email.com',  '081234567890'),
('Budi Santoso', 'budi@email.com',  '081234567891'),
('Citra Dewi',   'citra@email.com', '081234567892');

-- Insert data buku
INSERT INTO buku (judul, pengarang, penerbit, tahun_terbit, stok, kategori) VALUES
('Pemrograman MySQL',    'Agus Saputra',  'AUB Press',     2022, 5, 'Teknologi'),
('Algoritma & Struktur', 'Rinaldi Munir', 'Informatika',   2021, 3, 'Teknologi'),
('Harry Potter 1',       'J.K. Rowling',  'Gramedia',      2000, 2, 'Fiksi'),
('Bumi Manusia',         'Pramoedya',     'Lentera Dipas', 1980, 4, 'Sastra');

-- Insert data peminjaman
INSERT INTO peminjaman (id_anggota, id_buku, tgl_pinjam, tgl_kembali, status) VALUES
(1, 1, '2026-04-01', '2026-04-08', 'Dikembalikan'),
(1, 2, '2026-04-10', NULL,         'Dipinjam'),
(2, 3, '2026-04-05', '2026-04-12', 'Dikembalikan'),
(3, 1, '2026-04-15', NULL,         'Dipinjam');

-- Query: Tampilkan semua peminjaman aktif dengan info anggota dan buku
SELECT 
    a.nama          AS 'Nama Anggota',
    b.judul         AS 'Judul Buku',
    p.tgl_pinjam    AS 'Tanggal Pinjam',
    p.status        AS 'Status'
FROM peminjaman p
JOIN anggota a ON p.id_anggota = a.id_anggota
JOIN buku b    ON p.id_buku    = b.id_buku
WHERE p.status = 'Dipinjam'
ORDER BY p.tgl_pinjam;

-- Query: Hitung total buku per kategori
SELECT 
    kategori,
    COUNT(*) AS jumlah_judul,
    SUM(stok) AS total_stok
FROM buku
GROUP BY kategori
ORDER BY total_stok DESC;

-- Query: Anggota yang belum pernah meminjam
SELECT a.nama, a.email
FROM anggota a
LEFT JOIN peminjaman p ON a.id_anggota = p.id_anggota
WHERE p.id_pinjam IS NULL;
```

---

## 📝 Urutan Penulisan Query SELECT Lengkap

```sql
SELECT   kolom1, kolom2, ...    -- 1. Pilih kolom
FROM     nama_tabel             -- 2. Dari tabel mana
JOIN     tabel_lain ON ...      -- 3. Gabung tabel (opsional)
WHERE    kondisi                -- 4. Filter baris
GROUP BY kolom                  -- 5. Kelompokkan
HAVING   kondisi_group          -- 6. Filter hasil group
ORDER BY kolom ASC/DESC         -- 7. Urutkan
LIMIT    angka;                 -- 8. Batasi hasil
```

---

> 📌 **Dibuat untuk keperluan belajar mata kuliah Basis Data**  
> 🏫 **Universitas Dharma AUB Surakarta — Prodi Informatika**  
> ✍️ **Aura Rose — 2026**