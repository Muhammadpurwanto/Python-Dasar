brt = int(input('masukan berat mangga:'))
hrg = int(input('masukan harga mangga:'))
total_harga = brt * hrg
print('total belanja:',total_harga)
uang = int(input('masukan uang yang di bawa ibu:'))
ongkos= int(input('masukan ongkos angkot 1x perjalanan:'))

total_ongkos = ongkos * 2
total_belanja = total_harga + total_ongkos
print("total belanja ",total_belanja)
sisa_uang = uang - total_belanja
print(f"sisa uang {sisa_uang}")