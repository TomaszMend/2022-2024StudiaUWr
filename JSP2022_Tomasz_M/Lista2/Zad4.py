napis  = input("Podaj napis: ")
x = napis.replace(napis[0], "$") #zmienia wszystkie litery podobne do pierwszej w $
x = x.replace(x[0], napis[0],1) #zmnienia pierwszy znak w pierwsza litere oryginalnego slowa
print(x)