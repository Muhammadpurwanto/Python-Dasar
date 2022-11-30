'''fungsi dengan kembalian'''
import os
def kuadrat(x):
    hasil=x**2
    return hasil
y=kuadrat(3)

print(y)
print(kuadrat(6))

def operasi(x,y):
    tambah=x+y
    kurang=x-y
    kali=x*y
    bagi=x/y
    return tambah, kurang, kali, bagi

t,k,ka,b = operasi(3,5)
print(f"Hasil tambah = {t}")
print(f"Hasil kurang = {k}")
print(f"Hasil kali = {ka}")
print(f"Hasil bagi = {b}")



