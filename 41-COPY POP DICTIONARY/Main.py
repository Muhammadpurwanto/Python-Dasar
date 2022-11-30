# copy dictionary

teman2 = {
    "cup":"surucup",
    "tong":"sirotong",
    "dung":"sidudung"
}

friends = teman2.copy()
print(f"teman2: {teman2}\n")
print(f"friends: {friends}\n")

teman2["cup"]="siricip"
print(f"teman2: {teman2}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataCup = friends.pop("cup")
print(f"data ucup: {dataCup}")
print(f"friends: {friends}")

#popitem dictionary (data terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataTerakhir}")
print(f"friends: {friends}")




