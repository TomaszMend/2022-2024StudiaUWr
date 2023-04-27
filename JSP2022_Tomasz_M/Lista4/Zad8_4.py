def sumahar(n):
	s=0
	for i in range(1, n+1):
		s = s + 1/i;
	return s;
n = int(input("Podaj N: "))
print("Suma: ", sumahar(n))
