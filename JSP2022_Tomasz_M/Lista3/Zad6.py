
j = [1,2,3,4,5,6,7,8,9,10]
x = []
for i in range(10):
	print("Podaj liczbę całkowitą do tabliczki mnożenia poraz " , i+1 , " maksymalnie do 10 :")
	x.append(int(input("")))
for i in range(10):
	print("\t",j[i], end = '')
print("")

for i in range(10):
	print(x[i], end = '')
	for k in range(10) :
		print("\t", x[i]*j[k], end = '')
	print("")
