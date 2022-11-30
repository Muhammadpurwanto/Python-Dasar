import datetime

waktu=datetime.datetime.now()
print(f"datetime now: {waktu}")
print(f"waktu tahun: {waktu.year}")
print(f"hari: {waktu.strftime('%A')}")

from collections import Counter
data=['a','b','c','d','a','d','c']
hasil=0
for i in data:
    if 'a' == i:
        hasil+=1
        print(hasil)
data_count=Counter(data)
print(f"data count = {data_count}")
print(f"data count a = {data_count['a']}")
print(f"data count b = {data_count['b']}")

import io
file=io.open('file.txt','r')
print(file.read())



