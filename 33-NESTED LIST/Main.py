data_0 = [1,2]
data_1 = [3,4]

list_biasa = [1,2,3,4]
print(f"data list biasa = {list_biasa}")

list_2d = [data_0,data_1]
print(f"list 2d = {list_2d}")

# contoh penggunaan
peserta_0 = ["ucup",20,"laki-laki"]
peserta_1 = ["otong",19,"laki-laki"]
peserta_2 = ["marni",24,"perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(list_peserta)
print(f"Nama\t Umur\t Gender")
for peserta in list_peserta:
    print(f"{peserta[0]}\t {peserta[1]}\t{peserta[2]}")

