def silnia(n):
	il=1
	for i in range(1, n+1):
		il = il * i;
	return il;
n = int(input("Podaj N: "))
print("Suma: ", silnia(n))
