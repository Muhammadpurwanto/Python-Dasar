import datetime as dt

data_mahasiswa={}
mahasiswa1 = {
    'nama':'surucup',
    'nim':'0012345',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':dt.datetime(2000,3,23)
}
mahasiswa2 = {
    'nama':'surotong',
    'nim':'0012346',
    'sks_lulus':120,
    'beasiswa':False,
    'lahir':dt.datetime(2003,3,13)
}
mahasiswa3 = {
    'nama':'durudung',
    'nim':'0012346',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':dt.datetime(2001,5,4)
}

data_mahasiswa.update({
    'mah1':mahasiswa1,
    'mah2':mahasiswa2,
    'mah3':mahasiswa3
})
print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10}")
print(50*'=')

for mhs in data_mahasiswa.keys():
    KEY = mhs
    NAMA = data_mahasiswa.get(KEY)['nama']
    NIM = data_mahasiswa.get(KEY)['nim']
    SKS = data_mahasiswa.get(KEY)['sks_lulus']
    BEASISWA = data_mahasiswa.get(KEY)['beasiswa']
    LAHIR = data_mahasiswa.get(KEY)['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")





