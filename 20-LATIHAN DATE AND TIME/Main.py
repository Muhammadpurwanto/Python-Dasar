# Date and time

import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"hari ini hari: {hari_ini:%A}")

# tanggal = dt.date(2001,3,14)
# print(tanggal)

print("silahkan masukan tanggal, bulan, tahun")
tanggal = int(input("Tanggal ="))
bulan = int(input("Bulan\t="))
tahun = int(input("Tahun\t="))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah {tanggal_lahir}")
print(f"harinya adalah {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"umur anda adalah {umur_tahun} tahun {umur_bulan} bulan")
