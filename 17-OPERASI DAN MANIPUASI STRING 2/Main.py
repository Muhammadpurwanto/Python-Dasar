# operator dalam bentuk method
# merubah case dari string
# merubah huruf ke uppercase

salam = "bro!"
print("normal: ",salam)
salam = salam.upper()
print("upper: ",salam)

# merubah ke lower case
alay = "aKu KeCe AbiZZZzzzZZ"
print("normal: ",alay)
alay = alay.lower()
print("lower: ",alay)

# pengecekan dengan isX method
# contoh pengecekan lower case
salam = "sist"
apakahLower = salam.islower()
print(salam," is lower: ",str(apakahLower))
apakahUpper = salam.isupper()
print(salam," is upper: ",str(apakahUpper))

# isalpha() <-- untuk pengecekan huruf
# isalnum() <-- huruf dan angka
# isdecimal()<--angka saja
# isspace() <-- spasi, tab, newline
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cekJudul = judul.istitle()
print(judul," is title: ",str(cekJudul))

# ngecek komponen startswist() endswist()
cekStart = "Sangjangnim Oppa".startswith('Sangjangnim')
print("start: ",str(cekStart))

cekEnd = "Sangjangnim Oppa".endswith('Oppa')
print("end: ",str(cekEnd))

# penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = "aku,sayang,kamu"
print(gabungan.split(','))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'",kanan,"'")

kiri = "kiri".ljust(10)
print("'",kiri,"'")

tengah = "tengah".center(20,'*')
print("'",tengah,"'")

# kebalokannya--> strip()
tengah = tengah.strip("*")
print("'",tengah,"'")




