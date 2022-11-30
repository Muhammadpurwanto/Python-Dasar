# looping dari list

# for loop
kumpulan_angka = [4,3,2,1]
print('FOR LOOP')
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup","otong","dudung","dadang"]
for nama in peserta:
    print(f"nama = {nama}")


# for loop dan range
kumpulan_angka = [3,4,5,4,2,4,0]
panjang = len(kumpulan_angka)
print('\nFOR LOOP DAN RANGE')
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")


# while loop

kumpulan_angka = [3,4,5,4,2,4,0]
panjang = len(kumpulan_angka)
print('\nWHILE LOOP')

i =0
while i< panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i+=1

# list comprehensent
print('\nComperehension list')
data = ["ucup",1,2,3,"otong"]
[print(f"data = {i}") for i in data]

# enumerate
print('ENUMERATE')
data_list = ["ucup",12,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")








