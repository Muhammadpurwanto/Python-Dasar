'''Type hints fungsi'''
import string
def angka (argument:int)->int:
    hasil = 10**argument
    return hasil
total = angka(2)
print(total)

def display(argument:string)->string:
    print(argument)
muncul=display("ucup")


def kali(x:int,y:int)->int:
    hasil = x*y
    print(f"hasil perkalian antara {x} x {y} = {hasil}")

kali(4,8)


