#---LIST---

# kumpulan data numbers
data_angka = [1,2,3,4]
print(data_angka[2])

# kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False,True]
print(data_boolean)

# kumpulan campuran
data_campuaran = [1, "bala-bala", "cireng", True]
print(data_campuaran)

# cara alternatif membuat list
data_range = range(0,10,3) #range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop,list comprensent
list_for = [i for i in range(0,10)]
print(list_for)

# membuat list pake for dan if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 == 1]
print(list_for_if)



