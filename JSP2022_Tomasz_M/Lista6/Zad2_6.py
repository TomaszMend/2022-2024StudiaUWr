from SzyfrCezara import *
n=int(input("Wpisz numerycznie stopień szyfrowania kodu Cezara: "))
if n>25:
    n=25
if n<1:
    n=1
print("Wpisz zdanie do szyfrowania:")
tekst=input()
print(szyfr(n,tekst))
print(deszyfr(n,szyfr(n,tekst)))
