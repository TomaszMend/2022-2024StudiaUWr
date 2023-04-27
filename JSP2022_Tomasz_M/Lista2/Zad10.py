lista = [0]
for x in range(3, 100, 3):
    lista.append(x)
print(lst)
del(lista[5:len(lista):3])
print(lista)
print(sum(lista)/len(lista))