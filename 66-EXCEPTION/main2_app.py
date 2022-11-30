from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input pertama harus angka"
    return a+b
print(tambah(3,8))

angka=0
try:
    hasil =10/angka
except Exception as error_massage:
    print(error_massage)
