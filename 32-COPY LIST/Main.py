# teknik duplikat list

a = ['ucup','dadang','dudung']
print(f"a = {a}")
b = a
print(f"b = {b}")

# merubah member a
a[1]="ferdy"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari list
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# menduplikat list dengan copy
c = a.copy()
c[1]="eko"
print(f"a = {a}")
print(f"c = {c}")
print(f"addres a = {hex(id(a))}")
print(f"addres c = {hex(id(c))}")


