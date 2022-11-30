# '''fungsi biasa'''


# def fungsi(nama,tinggi,berat):
#     print(f"{nama} punya {tinggi} dan berat {berat}")

# fungsi("ucup",160,56)

# def fungsi(**kwargs):
#     nama = kwargs["nama"]
#     tinggi = kwargs["tinggi"]
#     berat = kwargs["berat"]
#     print(f"{nama} punya {tinggi} dan berat {berat}")


# fungsi(nama="ucup",tinggi=183,berat=67)



assigment = input("Tambah/kali: ")
def math (*args,**kwargs):
    if kwargs['option']=='tambah':
        print("operasi penjumlahan")
        jmlh=0
        for i in args:
            jmlh += i
        return jmlh
    elif kwargs['option']=='kali':
        print("operasi perkalian")
        jmlh=1
        for i in args:
            jmlh *= i
        return jmlh

hasil=math(1,2,3,4,5,option=assigment)
print(f"pertambahan: {hasil}")
# hasil=math(1,2,3,4,5,option=assigment)
# print(f"perkalian: {hasil}")
