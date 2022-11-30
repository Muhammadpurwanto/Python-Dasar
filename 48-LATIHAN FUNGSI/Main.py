'''latihan fungsi'''

import os
from tkinter import N

def header():
    os.system("cls")
    print(f"{'PROGAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'='*30:^40}")

def input_user():
    lebar = int(input("masukan nalai lebar: "))
    panjang = int(input("masukan nalai panjang: "))
    return lebar, panjang

def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    return 2*(lebar+panjang)

while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    print(f"hasil perhitungan luas = {LUAS}")
    print(f"hasil perhitungan keliling = {KELILING}")

    isCountinue = input("Apakah lanjut (y/n)? ")
    if isCountinue=="n":
        break

print("Progam selesai")
