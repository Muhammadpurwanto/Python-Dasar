# operasi dictionary

data_dict = {
    'cp' : 'ucup',
    'tg' : 'otong',
    'dd' : "dudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHEKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict: {CHEKKEY}")

# mengakses value (read) dengan get
print(data_dict["cp"])
print(data_dict.get('cp'))
# print(data_dict["kis"])
print(data_dict.get('kis', 'key tidak ditemukan'))

# update data
data_dict["cp"] = "surucup"
print(data_dict)

# menambah data
data_dict["sep"] = "asep"
print(data_dict)

data_dict.update({'cp':'markucup'})
print(data_dict)
data_dict.update({'ak':'markus'})
print(data_dict)

# delet
del data_dict['ak']
print(data_dict)
