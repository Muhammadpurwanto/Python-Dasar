# Global dan Local scope

nama_global = "otong" # <-variable global

# fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()
# loop
for i in range(0,5):
    print(f"loop ke {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variable local

def fungsi2():
    nama_local = "ucup" #<-variable local

fungsi2()
# print(nama_local) #<-tidak bisa dilakukan

## Contoh 1 penggunaan
def say_otong():
    print(f"Hello {nama}")

nama = "otong"
say_otong()

## contoh 2 merubah variable global
angka = 0
nama = "otong"

# variable local tidak bisa di rubah di dalam fungsi
def ubah_angka(nilai_baru):
    global angka # merubah menjadi variable global
    angka=nilai_baru
print(f"sebelum - {angka}")
ubah_angka(10)
print(f"setelah - {angka}")

def ubah_nama(nama_baru):
    global nama # merubah menjadi variable global
    nama=nama_baru
print(f"sebelum - {nama}")
ubah_nama("ucup")
print(f"setelah - {nama}")

# contoh 3
# untuk loop dan percabangan bisa merubah variable local
angka = 0
for i in range(0,5):
    angka +=1
    angka_dummy = 10

print(angka)
print(angka_dummy)

if True:
    angka_dummy = 5

print(angka_dummy)




