import tkinter as tk
import mysql.connector
from tkinter import messagebox

def hubungkan_mariadb():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aura2007",  # Ganti dengan password MySQL Anda jika ada
            database="kampus"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Koneksi Gagal", f"Error: {err}")
        return None

def buat_jendela_login():
    # 1. Inisialisasi Jendela Login
    login_win = tk.Tk()
    login_win.title("Login Sistem")
    login_win.geometry("300x200")
    login_win.eval('tk::PlaceWindow . center')
    login_win.configure(bg="#222222")

    # Fungsi Verifikasi Username & Password
    def verifikasi_login():
        username = entry_user.get()
        password = entry_pass.get()

        if username == "admin" and password == "akuhitam":
            messagebox.showinfo("Sukses", "Login Berhasil!")
            login_win.destroy()       # Tutup jendela login
            buka_aplikasi_utama()     # Buka aplikasi utama kesiswaan
        else:
            messagebox.showerror("Gagal", "Username atau Password salah!")

    # --- UI Jendela Login ---
    tk.Label(login_win, text="LOGIN SISTEM", fg="white", bg="#222222", font=("Calibri", 16, "bold")).pack(pady=10)

    # Input Username
    frame_user = tk.Frame(login_win, bg="#222222")
    frame_user.pack(pady=5)
    tk.Label(frame_user, text="Username:", fg="white", bg="#222222", width=10, anchor="w").pack(side=tk.LEFT)
    entry_user = tk.Entry(frame_user)
    entry_user.pack(side=tk.LEFT)

    # Input Password
    frame_pass = tk.Frame(login_win, bg="#222222")
    frame_pass.pack(pady=5)
    tk.Label(frame_pass, text="Password:", fg="white", bg="#222222", width=10, anchor="w").pack(side=tk.LEFT)
    entry_pass = tk.Entry(frame_pass, show="*") # Sensor password pakai tanda bintang
    entry_pass.pack(side=tk.LEFT)

    # Tombol Login
    btn_login = tk.Button(login_win, text="Login", bg="#68405F", fg="white", font=("Calibri", 11, "bold"), width=15, command=verifikasi_login)
    btn_login.pack(pady=15)

    login_win.mainloop()


def buka_aplikasi_utama():
    # 2. Inisialisasi Jendela Utama Kesiswaan
    root = tk.Tk()
    root.title("Aplikasi kesiswaan")
    root.geometry("400x550") # Tinggi disesuaikan biar teks box di bawah gak kepotong
    root.eval('tk::PlaceWindow . center')
    root.configure(bg="#333333")

    # --- LOGIK VALIDASI ---
    
    # Validasi Nama & Asal (Hanya boleh Huruf dan Spasi)
    def cek_huruf(text_input):
        # Mengizinkan string kosong (pas dihapus) atau teks yang isinya cuma huruf & spasi
        return text_input == "" or all(char.isalpha() or char.isspace() for char in text_input)

    # Validasi NIM (Hanya boleh Angka)
    def cek_angka(text_input):
        # Mengizinkan string kosong atau teks yang isinya cuma angka bulat
        return text_input == "" or text_input.isdigit()

    # Daftarkan fungsi validasi ke mesin Tkinter
    register_huruf = root.register(cek_huruf)
    register_angka = root.register(cek_angka)

    # Fungsi untuk membersihkan field (Tombol Clear)
    def clear_fields():
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        entry_asal.delete(0, tk.END)

    # Container Frame
    frame_input = tk.Frame(root) 
    frame_input.pack(anchor="w", pady=10, padx=15) 
    frame_input.configure(bg="#333333") 

    # --- BARIS 0: NAMA (Validasi Huruf) ---
    tk.Label(frame_input, text="Nama", fg="white", bg="#68405F", font=("Times New Roman", 14), width=8).grid(row=0, column=0, pady=10, sticky="w") 
    entry_nama = tk.Entry(
        frame_input, 
        font=("Calibri", 14),
        validate="key", # Dicek setiap kali user menekan tombol keyboard
        validatecommand=(register_huruf, "%P") # %P adalah status teks terbaru jika diizinkan
    )
    entry_nama.grid(row=0, column=1, padx=10)

    # --- BARIS 1: NIM (Validasi Angka) ---
    tk.Label(frame_input, text="NIM", fg="white", bg="#68405F", font=("Times New Roman", 14), width=8).grid(row=1, column=0, pady=10, sticky="w") 
    entry_nim = tk.Entry(
        frame_input, 
        font=("Calibri", 14),
        validate="key",
        validatecommand=(register_angka, "%P")
    )
    entry_nim.grid(row=1, column=1, padx=10)

    # --- BARIS 2: ASAL (Validasi Huruf) ---
    tk.Label(frame_input, text="Asal", fg="white", bg="#68405F", font=("Times New Roman", 14), width=8).grid(row=2, column=0, pady=10, sticky="w") 
    entry_asal = tk.Entry(
        frame_input, 
        font=("Calibri", 14),
        validate="key",
        validatecommand=(register_huruf, "%P")
    )
    entry_asal.grid(row=2, column=1, padx=10)

    # Fungsi untuk menampilkan data dari database ke text_display
    def tampilkan_data():
        text_display.delete("1.0", tk.END)
        conn = hubungkan_mariadb()
        if conn:
            try:
                cursor = conn.cursor()
                # Mengambil kolom NIM, Nama, dan Asal
                cursor.execute("SELECT NIM, Nama, Asal FROM mahasiswa")
                rows = cursor.fetchall()
                text_display.insert(tk.END, "NIM | Nama | Asal\n")
                text_display.insert(tk.END, "-" * 30 + "\n")
                for row in rows:
                    text_display.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Gagal membaca data: {err}")
            finally:
                conn.close()

    # Fungsi untuk menambahkan data baru ke database
    def tambah_data():
        nama = entry_nama.get().strip()
        nim = entry_nim.get().strip()
        asal = entry_asal.get().strip()
        
        if not nama or not nim or not asal:
            messagebox.showwarning("Input Kosong", "Semua field (Nama, NIM, Asal) harus diisi!")
            return
            
        conn = hubungkan_mariadb()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO mahasiswa (NIM, Nama, Asal) VALUES (%s, %s, %s)"
                values = (nim, nama, asal)
                cursor.execute(query, values)
                conn.commit()
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil ditambahkan!")
                clear_fields()
                tampilkan_data()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Gagal menambahkan data: {err}")
            finally:
                conn.close()

    # Sub-frame untuk tombol aksi
    frame_button_aksi = tk.Frame(frame_input, bg="#333333")
    frame_button_aksi.grid(row=3, column=1, pady=5, sticky="ew")

    # Tombol Tambah Data (Dihubungkan ke fungsi tambah_data)
    btn_tambah = tk.Button(frame_button_aksi, text="Tambah Data", bg="red", fg="white", font=("Calibri", 12), command=tambah_data)
    btn_tambah.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    # Tombol Clear
    btn_clear = tk.Button(frame_button_aksi, text="Clear", bg="gray", fg="white", font=("Calibri", 12), command=clear_fields)
    btn_clear.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    # Tombol Logout (Kembali ke halaman login)
    def kembali_ke_login():
        root.destroy()          # Tutup jendela utama
        buat_jendela_login()    # Buka lagi jendela login awal

    btn_logout = tk.Button(frame_input, text="Logout", bg="darkgrey", fg="white", font=("Calibri", 14, "bold"), command=kembali_ke_login)
    btn_logout.grid(row=4, column=1, pady=20, sticky="ew")

    # Kotak Teks Display bawah
    text_display = tk.Text(frame_input, width=22, height=8, font=("Calibri", 12), bg="#555555", fg="white")
    text_display.grid(row=5, column=1, pady=10, sticky="ew")

    # Tampilkan data secara otomatis saat jendela utama terbuka
    tampilkan_data()

    root.mainloop()


if __name__ == "__main__":
    # Jalankan aplikasi pertama kali langsung ke login screen
    buat_jendela_login()