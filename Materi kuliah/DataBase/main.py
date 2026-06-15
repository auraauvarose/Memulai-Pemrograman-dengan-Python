import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime
from tkcalendar import DateEntry


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

        if username == "musang" and password == "akuhitam":
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
    root.title("Aplikasi Kesiswaan")
    root.geometry("750x650")
    root.eval('tk::PlaceWindow . center')
    root.configure(bg="#333333")

    # --- LOGIK VALIDASI ---
    
    # Validasi Nama & Asal (Hanya boleh Huruf dan Spasi)
    def cek_huruf(text_input):
        return text_input == "" or all(char.isalpha() or char.isspace() for char in text_input)

    # Validasi NIM (Hanya boleh Angka)
    def cek_angka(text_input):
        return text_input == "" or text_input.isdigit()

    register_huruf = root.register(cek_huruf)
    register_angka = root.register(cek_angka)

    # Container Frame
    frame_input = tk.Frame(root, bg="#333333") 
    frame_input.pack(pady=15, padx=20, fill="both", expand=True) 

    # --- INPUT FIELDS (Row 0 - 4) ---
    
    # Baris 0: Nama
    tk.Label(frame_input, text="Nama", fg="white", bg="#68405F", font=("Times New Roman", 13, "bold"), width=14, anchor="w").grid(row=0, column=0, pady=5, sticky="w") 
    entry_nama = tk.Entry(frame_input, font=("Calibri", 13), width=25, validate="key", validatecommand=(register_huruf, "%P"))
    entry_nama.grid(row=0, column=1, padx=10, sticky="w")

    # Baris 1: NIM
    tk.Label(frame_input, text="NIM", fg="white", bg="#68405F", font=("Times New Roman", 13, "bold"), width=14, anchor="w").grid(row=1, column=0, pady=5, sticky="w") 
    entry_nim = tk.Entry(frame_input, font=("Calibri", 13), width=25, validate="key", validatecommand=(register_angka, "%P"))
    entry_nim.grid(row=1, column=1, padx=10, sticky="w")

    # Baris 2: Asal
    tk.Label(frame_input, text="Asal", fg="white", bg="#68405F", font=("Times New Roman", 13, "bold"), width=14, anchor="w").grid(row=2, column=0, pady=5, sticky="w") 
    entry_asal = tk.Entry(frame_input, font=("Calibri", 13), width=25, validate="key", validatecommand=(register_huruf, "%P"))
    entry_asal.grid(row=2, column=1, padx=10, sticky="w")
    
    # Baris 3: Jenis Kelamin
    tk.Label(frame_input, text="Jenis Kelamin", fg="white", bg="#68405F", font=("Times New Roman", 13, "bold"), width=14, anchor="w").grid(row=3, column=0, pady=5, sticky="w") 
    entry_jenis_kelamin = tk.Entry(frame_input, font=("Calibri", 13), width=25, validate="key", validatecommand=(register_huruf, "%P"))
    entry_jenis_kelamin.grid(row=3, column=1, padx=10, sticky="w")
    
    # Baris 4: Tanggal Masuk
    tk.Label(frame_input, text="Tanggal Masuk", fg="white", bg="#68405F", font=("Times New Roman", 13, "bold"), width=14, anchor="w").grid(row=4, column=0, pady=5, sticky="w") 
    entry_tanggal_masuk = DateEntry(
        frame_input, 
        font=("Calibri", 13),
        width=23,
        background="#68405F",
        foreground="white",
        borderwidth=2,
        date_pattern="yyyy-mm-dd"
    )
    entry_tanggal_masuk.grid(row=4, column=1, padx=10, sticky="w")

    # --- FUNGSI CRUD & HELPER ---

    # Fungsi untuk membersihkan field (Tombol Batal / Clear)
    def clear_fields():
        entry_nim.config(state="normal")
        entry_nim.delete(0, tk.END)
        entry_nama.delete(0, tk.END)
        entry_asal.delete(0, tk.END)
        entry_jenis_kelamin.delete(0, tk.END)
        entry_tanggal_masuk.set_date(datetime.date.today())
        
        # Reset state tombol
        btn_tambah.config(state="normal")
        btn_edit.config(state="disabled")
        btn_hapus.config(state="disabled")
        
        # Deselect item di tabel
        for item in tree.selection():
            tree.selection_remove(item)

    # Fungsi untuk menampilkan data dari database ke Treeview
    def tampilkan_data():
        # Bersihkan tabel terlebih dahulu
        for item in tree.get_children():
            tree.delete(item)
            
        conn = hubungkan_mariadb()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT NIM, Nama, Asal, Jenis_Kelamin, Tanggal_Masuk FROM mahasiswa")
                rows = cursor.fetchall()
                for row in rows:
                    tgl = row[4].strftime('%Y-%m-%d') if isinstance(row[4], (datetime.date, datetime.datetime)) else str(row[4]) if row[4] else ""
                    jk = row[3] if row[3] else ""
                    tree.insert("", tk.END, values=(row[0], row[1], row[2], jk, tgl))
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Gagal membaca data: {err}")
            finally:
                conn.close()

    # Fungsi untuk menambahkan data baru ke database
    def tambah_data():
        nama = entry_nama.get().strip()
        nim = entry_nim.get().strip()
        asal = entry_asal.get().strip()
        jenis_kelamin = entry_jenis_kelamin.get().strip()
        tanggal_masuk = entry_tanggal_masuk.get().strip()

        if not nim or not nama or not asal or not jenis_kelamin or not tanggal_masuk:
            messagebox.showwarning("Input Kosong", "Semua field input harus diisi!")
            return
            
        conn = hubungkan_mariadb()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO mahasiswa (NIM, Nama, Asal, Jenis_Kelamin, Tanggal_Masuk) VALUES (%s, %s, %s, %s, %s)"
                values = (nim, nama, asal, jenis_kelamin, tanggal_masuk)
                cursor.execute(query, values)
                conn.commit()
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil ditambahkan!")
                clear_fields()
                tampilkan_data()
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    messagebox.showerror("Duplicate Key", f"Gagal menambahkan data:\nNIM '{nim}' sudah terdaftar!")
                else:
                    messagebox.showerror("Database Error", f"Gagal menambahkan data: {err}")
            finally:
                conn.close()

    # Fungsi untuk memperbarui data
    def edit_data():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Silakan pilih data pada tabel terlebih dahulu!")
            return
            
        entry_nim.config(state="normal")
        nim = entry_nim.get().strip()
        entry_nim.config(state="disabled")
        
        nama = entry_nama.get().strip()
        asal = entry_asal.get().strip()
        jenis_kelamin = entry_jenis_kelamin.get().strip()
        tanggal_masuk = entry_tanggal_masuk.get().strip()
        
        if not nama or not asal or not jenis_kelamin or not tanggal_masuk:
            messagebox.showwarning("Input Kosong", "Semua field input harus diisi!")
            return
            
        conn = hubungkan_mariadb()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE mahasiswa SET Nama=%s, Asal=%s, Jenis_Kelamin=%s, Tanggal_Masuk=%s WHERE NIM=%s"
                values = (nama, asal, jenis_kelamin, tanggal_masuk, nim)
                cursor.execute(query, values)
                conn.commit()
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil diubah!")
                clear_fields()
                tampilkan_data()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Gagal mengubah data: {err}")
            finally:
                conn.close()

    # Fungsi untuk menghapus data
    def hapus_data():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Silakan pilih data pada tabel terlebih dahulu!")
            return
            
        entry_nim.config(state="normal")
        nim = entry_nim.get().strip()
        entry_nim.config(state="disabled")
        
        konfirmasi = messagebox.askyesno("Konfirmasi Hapus", f"Apakah Anda yakin ingin menghapus data dengan NIM {nim}?")
        if not konfirmasi:
            return
            
        conn = hubungkan_mariadb()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM mahasiswa WHERE NIM=%s"
                cursor.execute(query, (nim,))
                conn.commit()
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil dihapus!")
                clear_fields()
                tampilkan_data()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Gagal menghapus data: {err}")
            finally:
                conn.close()

    # --- TOMBOL AKSI (Row 5) ---
    frame_button_aksi = tk.Frame(frame_input, bg="#333333")
    frame_button_aksi.grid(row=5, column=0, columnspan=2, pady=15, sticky="ew")

    btn_tambah = tk.Button(frame_button_aksi, text="Tambah", bg="#28a745", fg="white", font=("Calibri", 12, "bold"), command=tambah_data, width=10)
    btn_tambah.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    btn_edit = tk.Button(frame_button_aksi, text="Edit", bg="#007bff", fg="white", font=("Calibri", 12, "bold"), command=edit_data, width=10, state="disabled")
    btn_edit.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    btn_hapus = tk.Button(frame_button_aksi, text="Hapus", bg="#dc3545", fg="white", font=("Calibri", 12, "bold"), command=hapus_data, width=10, state="disabled")
    btn_hapus.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    btn_batal = tk.Button(frame_button_aksi, text="Batal", bg="#6c757d", fg="white", font=("Calibri", 12, "bold"), command=clear_fields, width=10)
    btn_batal.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    # --- TABEL / TREEVIEW DATA (Row 6) ---
    
    # Kustomisasi Style Treeview agar serasi tema gelap
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", 
                    background="#444444", 
                    foreground="white", 
                    fieldbackground="#444444", 
                    rowheight=25,
                    font=("Calibri", 11))
    style.map("Treeview", background=[("selected", "#68405F")])
    style.configure("Treeview.Heading", background="#68405F", foreground="white", font=("Calibri", 11, "bold"))

    columns_table = ("nim", "nama", "asal", "jenis_kelamin", "tanggal_masuk")
    tree = ttk.Treeview(frame_input, columns=columns_table, show="headings", height=8)
    
    tree.heading("nim", text="NIM")
    tree.heading("nama", text="Nama")
    tree.heading("asal", text="Asal")
    tree.heading("jenis_kelamin", text="Jenis Kelamin")
    tree.heading("tanggal_masuk", text="Tanggal Masuk")
    
    tree.column("nim", width=100, anchor="center")
    tree.column("nama", width=150, anchor="w")
    tree.column("asal", width=120, anchor="w")
    tree.column("jenis_kelamin", width=120, anchor="center")
    tree.column("tanggal_masuk", width=120, anchor="center")

    tree.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

    # Scrollbar untuk tabel
    scrollbar = ttk.Scrollbar(frame_input, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=6, column=2, sticky="ns", pady=10)

    # Logika ketika baris pada tabel dipilih
    def on_tree_select(event):
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, "values")
            if values:
                # Aktifkan NIM sementara untuk mengisi data
                entry_nim.config(state="normal")
                entry_nim.delete(0, tk.END)
                entry_nim.insert(0, values[0])
                # Nonaktifkan agar NIM tidak bisa diubah (Primary Key)
                entry_nim.config(state="disabled")
                
                entry_nama.delete(0, tk.END)
                entry_nama.insert(0, values[1])
                
                entry_asal.delete(0, tk.END)
                entry_asal.insert(0, values[2])
                
                entry_jenis_kelamin.delete(0, tk.END)
                entry_jenis_kelamin.insert(0, values[3])
                
                try:
                    date_val = datetime.datetime.strptime(values[4], "%Y-%m-%d").date()
                    entry_tanggal_masuk.set_date(date_val)
                except Exception:
                    pass
                
                # Mengubah status tombol
                btn_tambah.config(state="disabled")
                btn_edit.config(state="normal")
                btn_hapus.config(state="normal")

    tree.bind("<<TreeviewSelect>>", on_tree_select)

    # --- TOMBOL LOGOUT (Row 7) ---
    def kembali_ke_login():
        root.destroy()
        buat_jendela_login()

    btn_logout = tk.Button(frame_input, text="Logout", bg="#4e4e4e", fg="white", font=("Calibri", 12, "bold"), command=kembali_ke_login)
    btn_logout.grid(row=7, column=0, columnspan=2, pady=15, sticky="ew")

    # Tampilkan data secara otomatis saat jendela utama terbuka
    tampilkan_data()

    root.mainloop()


if __name__ == "__main__":
    # Jalankan aplikasi pertama kali langsung ke login screen
    buat_jendela_login()