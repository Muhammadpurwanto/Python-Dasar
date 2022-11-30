# exception akan terjadi saat progam
# mengalami error saat runtime

# input_user = int(input("masukan angka: "))
# hasil = None
# try:
#     hasil = 10/input_user
# except:
#     print("tidak boleh angka 0")
# print(f"hasil = {hasil}")

while True:
    angka = int(input("masukan angka pembagi: "))
    try:
        hasil=10/angka
        print("hasil:",hasil)
        is_done = input("mau lanjut(y/n)? ")
        if is_done=='n':
            break
    except:
        print("angka 0, masukan angka lagi")
print("akhir dari progam 1")

while True:
    try:
        with open("data.txt", mode="r", encoding="utf-8") as file:
            print(file.read())
            break
    except:
        with open("data.txt", mode="w",encoding='utf-8') as file:
            file.write("data baru")
            break
print("akhir dari progam 2")


