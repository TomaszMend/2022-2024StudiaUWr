print("Podaj ilość kolumn")
j = int(input())
print("Podaj ilość wierszów")
x = int(input())
for i in range(j):
	print("\t",i+1, end = '')
print("")

for i in range(x):
	print(i+1, end = '')
	for k in range(j) :
		print("\t", (k+1)*(i+1), end = '')
	print("")
