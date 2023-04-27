import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
print("Pierwiastki równania 'a*x^2 + b*x + c = 0' to: ")
delta = b*b - 4*a*c
if delta<0 :
	print("Równanie z podanymi a,b,c nie posiada pierwiastków")
if delta==0 :
	wynik = (-b)/(a*2)
	print("Delta wynosi 0 więc jedynym pierwiastkiem równania jest: ")
	print(wynik)
if delta>0 :
	sdelta = math.sqrt(delta)
	wynik1 = ((-b)-sdelta)/(a*2)
	wynik2 = ((-b)+sdelta)/(a*2)
	print("Twoimi pierwiastkami są: ")
	print("x1 = ", wynik1) 
	print("x2 = ", wynik2) 

