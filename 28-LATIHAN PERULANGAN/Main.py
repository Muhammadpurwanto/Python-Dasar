# latihan perulangan membuat segitiga

sisi = 4

# menggunakan for
# dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count+=1
print('akhir dari for')

# menggunakan while

count =1
while True:
    print("*"*count)
    count +=1

    if count > sisi:
        break
print('akhir dari while')

# hanya ganjil saja
# count =1
# while True:
#     if count%2:
#         print("*"*count)
#         count +=1
#     else:
#         count +=1
#         continue


#     if count > sisi:
#         break
# print('akhir dari while')













