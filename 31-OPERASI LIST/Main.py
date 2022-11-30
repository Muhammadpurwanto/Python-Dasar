data_angka = [1,3,5,23,4,5,4,3,]
print(f"data = {data_angka}")

# count data
jml_data_4 = data_angka.count(4)
jml_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jml_data_4}")
print(f"jumlah angka 3 = {jml_data_3}")

# ambil posisi data
data = ["ucup","otong","dadang"]
print(f"data = {data}")

index_dudung = data.index("dadang")
print(10*"=")
print(f"data = {index_dudung}")

# mengurutkan list
print(f"sebelum di sort = {data_angka}")
data_angka.sort()
print(f"setelah di sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f"sort data = {data}")

# membalik data
data_angka.reverse()
data.reverse()
print(f"data di reverse = {data_angka}")
print(f"data di reverse = {data}")


