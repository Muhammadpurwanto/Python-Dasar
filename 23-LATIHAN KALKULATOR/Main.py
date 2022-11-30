# Latihan percabangan
# Kalkulator sederhana

angka_1 = float(input("masukan angka 1: "))
operator = input("operator +,-,x,/: ") # bagian yg akan menentukan menjalankan aksi
angka_2 = float(input("masukan angka 2: "))

# Percabangan
if operator=="+":   # saat user memasukan operator (+) maka akan menjalankan ini
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator=="-": # saat user memasukan operator (-) maka akan menjalankan ini
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator=="/": # saat user memasukan operator (/) maka akan menjalankan ini
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
elif operator=="x": # saat user memasukan operator (x) maka akan menjalankan ini
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
else: # ketika user salah memasukan operator yang tidak sesuai
    print("anda salah memasukan nilai")
print("selesai")





