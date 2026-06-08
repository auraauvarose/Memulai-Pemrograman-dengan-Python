import tkinter as tk
from tkinter import messagebox # massagebox digunakan untuk menampilkan pesan peringatan, informasi, atau konfirmasi kepada pengguna dalam bentuk jendela pop-up. Ini sangat berguna untuk memberikan umpan balik kepada pengguna atau meminta konfirmasi sebelum melakukan tindakan tertentu.

# ── Credentials login ──────────────────────────────────────────────
USERNAME = "admin"
PASSWORD = "1234"

# ══════════════════════════════════════════════════════════════════
#  HALAMAN UTAMA
# ══════════════════════════════════════════════════════════════════
def show_main(root):
    # Bersihkan semua widget lama
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Aplikasi Kesiswaan")
    root.geometry("400x380")
    root.configure(bg="darkblue")

    frame = tk.Frame(root, bg="green", padx=15, pady=15)
    frame.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

    # ── Input fields ──
    lbl_nama = tk.Label(frame, text="Nama :", bg="black", fg="white",
                        font=("Arial", 11, "bold"), width=8, anchor="w")
    lbl_nama.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_nama = tk.Entry(frame, font=("Arial", 11), width=25)
    entry_nama.grid(row=0, column=1, padx=5, pady=5)

    lbl_nim = tk.Label(frame, text="NIM :", bg="black", fg="white",
    font=("Arial", 11, "bold"), width=8, anchor="w")
    lbl_nim.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_nim = tk.Entry(frame, font=("Arial", 11), width=25)
    entry_nim.grid(row=1, column=1, padx=5, pady=5)

    lbl_asal = tk.Label(frame, text="Asal :", bg="black", fg="white",
                        font=("Arial", 11, "bold"), width=8, anchor="w")
    lbl_asal.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_asal = tk.Entry(frame, font=("Arial", 11), width=25)
    entry_asal.grid(row=2, column=1, padx=5, pady=5)

    # ── Text display ──
    text_display = tk.Text(frame, width=30, height=5,
        font=("Arial", 10, "bold"), bg="white", fg="black")
    text_display.grid(row=6, column=1, pady=10, sticky="w")

    # ── Button callbacks ──
    def tambah_data():
        nama  = entry_nama.get().strip()
        nim   = entry_nim.get().strip()
        asal  = entry_asal.get().strip()
        if not nama or not nim or not asal:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        text_display.insert(tk.END, f"Nama: {nama} | NIM: {nim} | Asal: {asal}\n")

    def clear_data():
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        entry_asal.delete(0, tk.END)
        text_display.delete("1.0", tk.END)

    def save_data():
        content = text_display.get("1.0", tk.END).strip()
        if not content:
            messagebox.showinfo("Info", "Tidak ada data untuk disimpan.")
            return
        with open("data_siswa.txt", "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Sukses", "Data berhasil disimpan ke data_siswa.txt")

    def logout():
        if messagebox.askyesno("Logout", "Yakin ingin logout?"):
            show_login(root)

    # ── Buttons ──
    btn_tambah = tk.Button(frame, text="Tambah Data", bg="grey", fg="white",
    font=("Arial", 10, "bold"), command=tambah_data)
    btn_tambah.grid(row=3, column=1, padx=5, pady=10, sticky="w")

    btn_clear = tk.Button(frame, text="Clear", bg="grey", fg="white",
    font=("Arial", 10, "bold"), width=8, command=clear_data)
    btn_clear.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    btn_logout = tk.Button(frame, text="Logout", bg="red", fg="white",
    font=("Arial", 10, "bold"), width=8, command=logout)
    btn_logout.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    btn_save = tk.Button(frame, text="Save", bg="green", fg="white",
    font=("Arial", 10, "bold"), width=8, command=save_data)
    btn_save.grid(row=5, column=1, padx=5, pady=5, sticky="we")


# ══════════════════════════════════════════════════════════════════
#  HALAMAN LOGIN
# ══════════════════════════════════════════════════════════════════
def show_login(root):
    # Bersihkan semua widget lama
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Login – Aplikasi Kesiswaan")
    root.geometry("360x280")
    root.configure(bg="darkblue")

    # ── Outer frame ──
    frame = tk.Frame(root, bg="green", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # ── Judul ──
    lbl_title = tk.Label(frame, text="APLIKASI KESISWAAN",
    bg="green", fg="white",
    font=("Arial", 13, "bold"))
    lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # ── Username ──
    lbl_user = tk.Label(frame, text="Username :", bg="black", fg="white",
                        font=("Arial", 11, "bold"), width=10, anchor="w")
    lbl_user.grid(row=1, column=0, padx=5, pady=6, sticky="w")
    entry_user = tk.Entry(frame, font=("Arial", 11), width=18)
    entry_user.grid(row=1, column=1, padx=5, pady=6)
    entry_user.focus()

    # ── Password ──
    lbl_pass = tk.Label(frame, text="Password :", bg="black", fg="white",
                        font=("Arial", 11, "bold"), width=10, anchor="w")
    lbl_pass.grid(row=2, column=0, padx=5, pady=6, sticky="w")
    entry_pass = tk.Entry(frame, font=("Arial", 11), width=18, show="*")
    entry_pass.grid(row=2, column=1, padx=5, pady=6)

    # ── Pesan error ──
    lbl_error = tk.Label(frame, text="", bg="green", fg="yellow",
                         font=("Arial", 9, "italic"))
    lbl_error.grid(row=3, column=0, columnspan=2)

    # ── Login callback ──
    def do_login(event=None):
        u = entry_user.get().strip()
        p = entry_pass.get().strip()
        if u == USERNAME and p == PASSWORD:
            show_main(root)
        else:
            lbl_error.config(text="Username atau password salah!")
            entry_pass.delete(0, tk.END)

    # ── Tombol Login ──
    btn_login = tk.Button(frame, text="Login", bg="darkblue", fg="white",
    font=("Arial", 11, "bold"), width=18,
    command=do_login)
    btn_login.grid(row=4, column=0, columnspan=2, pady=(12, 0))

    # Enter key juga bisa login
    root.bind("<Return>", do_login)

    # ── Hint kredensial (hapus di produksi) ──
    lbl_hint = tk.Label(frame, text="(user: admin | pass: 1234)",
                        bg="green", fg="#ccffcc", font=("Arial", 8))
    lbl_hint.grid(row=5, column=0, columnspan=2, pady=(6, 0))
    


# ══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════
root = tk.Tk()
show_login(root)
root.mainloop()