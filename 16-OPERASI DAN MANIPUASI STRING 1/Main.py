# operasi dan manipulasi string
# 1. menyambung string (concatenate)

namaPertama = "ucup"
namaTengah = "D"
namaAkhir = "fame"

namaLengkap = namaPertama+" "+namaTengah+" "+namaAkhir
print(namaLengkap)

# 2. Menghitung panjang dari string
panjang = len(namaLengkap)
print(panjang)

# 3. Operatpr untuk string
d = "d"
status = d in namaLengkap
print(status)

d = "d"
status = d not in namaLengkap
print(status)

# mengulang string
print("wk"*10)

# indexing
print("index ke-0: "+namaLengkap[0])
print("index ke-(-1): "+namaLengkap[-1])
print("index ke-[0:3]: "+namaLengkap[0:4])

# item paling kecil
print("paling kecil: "+min(namaLengkap))

# item paling besar
print("paling besar: "+max(namaLengkap))

ascii_code = ord(" ")
print("ascii code spasi: ",str(ascii_code))

# 4. Operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jml o pada data ",data,"=",str(jumlah))