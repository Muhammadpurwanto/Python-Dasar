'''Lambda fanction'''

def f_kuadrat(angka):
    return angka**2
print(f"hasil fungsi kuadrad {f_kuadrat(3)}")

# dengan lambda
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat {kuadrat(3)}")

pangkat = lambda num,pow:num**pow
print(f"hasil pangkat {pangkat(6,2)}")

# sorting untuk list biasa
data_list = ["otong","ucup","dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting by len
data_list.sort(key=len)
print(f"sorted lis by len = {data_list}")

# sorting pakai panang
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama)
print(data_list)

# sort pakai lamba
data_list = ["otong","ucup","dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted lis by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka<5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)
data_angka_baru = list(filter(lambda x:x<5,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x%2==0),data_angka))
print(data_3)

# Anonymous function
# currying <--Haskell Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil
data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
print(pangkat(2)(5))














