import datetime
import os
import string
import random
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}
while True:

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

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<8} {'SKS':^3} {'LAHIR':^10}")
    print(50*'=')
    for mhs in data_mahasiswa:
        KEY = mhs
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^3} {LAHIR:^10}")

    print("\n")
    is_done = input("Apakah mau lanjut (y/n):")
    if is_done == "n":
        break
print("Akhir dari progam")


