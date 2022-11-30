'''Default argument'''

def say_hello(nama="kamu"):
    print(f"Hallo {nama}")

say_hello("ucup")
say_hello()

def sapa_dia(nama="kamu", pesan='apa kabar'):
    print(f"hallo {nama}, {pesan}")

sapa_dia("otong", "how are you")
sapa_dia()

def pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil
print(pangkat(5,2))
hasil = pangkat(pangkat=4,angka=2)
print(hasil)





