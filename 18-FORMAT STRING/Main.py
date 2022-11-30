# format string

# contoh generic
# string
name = "marline"
format_str = f"hello {name}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = "angka = ",angka
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 200000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:09.2f}"
print(format_str)

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = 10
format_minus = f"angka minus = {angka_minus:+d}"
format_plus = f"angka plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika
harga = 10000
jumlah = 5
format_str = f"harga total = {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hex)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)









