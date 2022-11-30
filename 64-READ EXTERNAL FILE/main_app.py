## membaca file external

print(3*'=',' membaca file ',3*'=')
file = open('data.txt',mode='r')

# mengecek kondisi
# print(file.readable())

# baca seluruh baris
print(file.read())

# # baca perbaris
# print(file.readline(),end="")
# print(file.readline(),end="")

# baca semua baris sebagai list
# print(file.readlines())

print("apakah file sudah di close:", file.closed)
file.close()
print("apakah file sudah di close:", file.closed)

print(3*'=',' membaca file dengan with ',3*'=')
with open('data.txt', mode="r") as file:
    content = file.readline()
    print(content, end="")
    print("apakah file sudah di close:", file.closed)
print("apakah file sudah di close:", file.closed)
    