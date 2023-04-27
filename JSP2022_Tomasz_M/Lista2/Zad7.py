from operator import itemgetter
#"Return a callable object that fetches item from its operand using the operand’s __getitem__() method. If multiple items are specified, returns a tuple of lookup values."
lista = [(2,8),(5,5),(9,3),(1, 0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
print(sorted(lista, key=itemgetter(1,0)))