
def szyfrowanie(x):
    c=[]
    klucz = {"a": "y", "e": "i", "i":"o","o":"a","y":"e"}
    for i in range(0,len(x)):
        if x[i] in klucz:
            c[i]=klucz[x[i]]
        else:
            c[i]=x[i]
    "".join(c)
    return c
def deszyfrowanie(x):
    klucz = {"y":"a","i":"e","o":"i","a":"o","e":"y"}
    for i in range(0,len(x)):
        if x[i] in klucz[x[i]]:
            c[i] = klucz[x[i]]
        else:
            c[i]=x[i]
    "".join(c)
    return c
slowo="ogorek"
zdanie="Ziemniak rosnie w ziemi na polu uprawnym"
mysli="mysli me, mysli twe, mysli nasze"
print(slowo)
szyfrowanie(slowo)
print(slowo)
deszyfrowanie(slowo)
print("")
print(zdanie)
szyfrowanie(zdanie)
print(zdanie)
deszyfrowanie(zdanie)
print("")
print(mysli)
szyfrowanie(mysli)
print(mysli)
deszyfrowanie(mysli)
print("")
