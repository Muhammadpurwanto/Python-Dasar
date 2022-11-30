# width and multiline

# data

data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 150.1
data_nomer_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomer sepatu = {data_nomer_sepatu}"
print(5*"="+"Data"+5*"=")
print(data_string)

# string multiline
data_nama = "ucup"
data_string = f"""
name   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomer_sepatu:>5}
"""
print(5*"="+"Data"+5*"=")
print(data_string)


