lista=[1,5,2,9]
print(lista)
sum=0
il=1
for x in range(len(lista)):
    sum=lista[x]+sum
    il=lista[x]*il
print(sum)
print(il)