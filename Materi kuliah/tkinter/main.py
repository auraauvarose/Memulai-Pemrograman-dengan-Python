import tkinter as tk

root = tk.Tk()
root.title("Hello, Tkinter!")
root.geometry("300x200")
root.eval('tk::PlaceWindow . center')
root.config(bg="lightblue")

# cara membuat frame input menjadi anak root
frame_input = tk.Frame(root)
frame_input.pack(anchor="W", pady=10)
frame_input.configure(bg="lightblue")
tk.Label(frame_input, text="Masukkan Nama:", bg="lightblue").pack(side="left", padx=5)

root.mainloop()

# ini buat windows kontol