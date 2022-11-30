""""fungsi dengan argument"""

def hello_world(nama):
    print(f"selamat datang dunia wahai {nama}")

hello_world("ucup")

def tambah(angka1, angka2):
    hasil = angka1+angka2
    print(f"hasil dari {angka1} + {angka2} = {hasil}")

tambah(2,8)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"selamat datang {peserta}")
data = ['alif', 'andi', 'ardi']
say_hi(data)

