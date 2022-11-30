# progam list buku

import os
list_buku = []
while True:
    os.system("cls")
    print("Masukan data buku")
    judul = input("masukan judul buku\t: ")
    penulis = input("masukan nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    


    isLanjut = input("Apakah dilanjut?(Y/n)")
    if isLanjut =='n':
        break

os.system("cls")
print(f"{'No.':<2}| {'Judul':<20} | {'Penulis':<20}")
for index,buku in enumerate(list_buku):
    print(f"{index+1:<2} | {buku[0]:<20} | {buku[1]:<20} ")

print("Progam selesai")








