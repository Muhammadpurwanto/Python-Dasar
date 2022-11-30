# 1.Mode write
# dia akan selalu membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("jhony is come back")
with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("ucup surucup")

# 2.mode append

with open("data2.txt", mode="w", encoding="utf-8") as file:
    file.write("jhony is come back\n")
with open("data2.txt", mode="a", encoding="utf-8") as file:
    file.write("ucup surucup")

    # 3.mode r+
with open("data3.txt", mode="w", encoding="utf-8") as file:
    file.write("ini adalah data ketiga")
with open("data3.txt", mode="r+", encoding="utf-8") as file:
    data = file.read()
    print(data)
    file.write("menambah dengan r+")
