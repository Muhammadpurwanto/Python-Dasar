'''*args'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("ucup",160,50)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong", 120, 40])

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dadang", 130, 40)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output
hasil = tambah(1,2,3,4,5,6)
print(hasil)
hasil = tambah(31,3,6)
print(hasil)

def hobi(*suka):
    nama = suka[0]
    hobi = suka[1]
    umur = suka[2]
    print(f"nama saya {nama} hobi saya {hobi} umur saya {umur}")

print(hobi('ucup','makan',21))





