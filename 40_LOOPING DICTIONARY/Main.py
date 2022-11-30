# looping dictionary

teman2 = {
    "cup":"ucup",
    "tong":"otong",
    "dung":"duudng",
    "sep":"asep"
}
# looping first try(yang keluar adalah key nya)

for teman in teman2:
    print(teman)

# operator untuk mengambil item/iterable
keys = teman2.keys()
print(keys)
for key in keys:
    print(teman2.get(key))

values = teman2.values()
print(values)
for value in values:
    print(value)

items = teman2.items()
print(items)
for item in items:
    print(item)

for key, value in items:
    print(f"key: {key}, value: {value}")











