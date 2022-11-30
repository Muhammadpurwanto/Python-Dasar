data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(f"data      = {data_2d}")
print(f"data copy = {data_2d_copy}")

# mengambil data
data = data_2d[0][1]
print(f"data = {data}")

# addres semuanya
print(f"addres data 2d      = {hex(id(data_2d))}")
print(f"addres data copy 2d = {hex(id(data_2d_copy))}")

# addres dari member
print(f"addres asli = {hex(id(data_2d[0]))}")
print(f"addres copy = {hex(id(data_2d_copy[0]))}")

# kita gunakan deepcopy
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
print(f"addres data 2d          = {hex(id(data_2D))}")
print(f"addres data deepcopy 2d = {hex(id(data_2D_deepcopy))}")

data_2d[0][1]=8
print(f"data 2d          = {data_2d}")
print(f"data 2d copy     = {data_2d_copy}")
print(f"data 2d deepcopy = {data_2D_deepcopy}")



