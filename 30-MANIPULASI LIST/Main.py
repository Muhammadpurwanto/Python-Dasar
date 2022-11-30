# manipulasi list

data = ["ucup","otong","dudung"]

# mengambil data dari list
# data_0 = data[0]
# print(f"data pertama {data_0}")
# print(len(data))

# menambahkan item pada list
print(f'\ndata sebelum ditambah\n {data}')
data.insert(1,"asep")
print(f"\ndata sesudah ditambah \n{data}")

# menambah di akhir list
data.append("jajang")
print(f"\ndata ditambah di akhir \n\n{data}")

#menambah list dengan list
data_baru = ["ujang","asep","dadang"]
data.extend(data_baru)
print(f"\ndata di extend\n {data}")

# merubah data
data[2] = "michel"
print(f"\ndata rubah \n{data}")

# meremove data
data.remove("ujang")
print(f"data remove {data}")

# meremove data paling belakang
data.pop()
print(f"\ndata paling belakang hilang \n{data}")
