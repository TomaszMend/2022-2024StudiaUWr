import math
a=int(input("Jaka chcesz dostac wysokosc?: "))
for i in range(a):
	for j in range(a-i+1):
		print(end=" ")
	for j in range(i+1):
		print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)), end=" ")
	print("\n")
