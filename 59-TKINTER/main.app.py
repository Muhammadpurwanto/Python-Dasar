#GUI-> Graphical User Interface

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg='black')
window.geometry('300x200')
window.resizable(False,False)
window.title("Belajar Python")

#frame input
input_frame = ttk.Frame(window)
# penempatan Grid, pack,place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="nama depan")
nama_depan_label.pack(padx=10,pady=10,fill='x',expand=True)
# 2. entry nama depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=10,fill='x',expand=True)
# 2. entry nama depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=10,fill='x',expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="nama belakang")
nama_belakang_label.pack(padx=10,pady=10,fill='x',expand=True)
# 4. entry nama belakang
NAMA_BELAKANG= tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,pady=10,fill='x',expand=True)
# 5. Tombol
def tombol_click():
    print("Ucup")
tombol_sapa = ttk.Button(input_frame,text="sapa!!",command=tombol_click)
tombol_sapa.pack(fill='x', expand=True, padx=10,pady=10)

window.mainloop()

