import datetime
import os

mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system('cls')
print(f"{'SELAMAT DATANG':^50}")
print(f"{'DATA MAHASISWA':^50}")
print(f"{20*'=':^50}")

mahasiswa = dict.fromkeys(mahasiswa_template.keys())


mahasiswa['nama'] = input("Masukan nama:")
mahasiswa['nim'] = input("Masukan NIM:")
mahasiswa['sks_lulus'] = int(input("SKS lulus:"))
TAHUN_LAHIR = int(input("Tahun lahir (YYYY):"))
BULAN_LAHIR = int(input("Bulan lahir (1-12):"))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31):"))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)




