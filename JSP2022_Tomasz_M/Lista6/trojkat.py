from __future__ import division
def rownosc(a,b,c):
	if a == b and b == c:
		return "rownoboczny"
	if (a == b and b != c) or ( a == c and c != b) or (b==c and c!=a):
		return "rownoramienny"
	if a != b and b != c and c != a :
		return "różnoboczny"
def obwod(a,b,c):
	return a+b+c
def pole(a,b,c):
	return float((a*b*c)/(a*2))
def typ(a,b,c):
	max=0
	if a>max :
		max=a
		q=b
		w=c
	if b>max :
		max=b
		q=a
		w=c
	if c>max :
		max=c
		q=b
		w=a
	if max*max == q*q+w*w :
		return "prostokątny"
	if max*max > q*q+w*w :
		return "rozwartokątny"
	if max*max < q*q+w*w :
		return "ostrokątny"

		
	
