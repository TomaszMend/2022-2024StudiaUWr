print("Do którego argumentu ma działać ciąg Fibonacciego?")
arg=int(input())
Fib=[]

for i in range(0,arg):
	if(i>1):
		Fib.append(Fib[i-1]+Fib[i-2])
	if(i==0):
		Fib.append(0)
	if(i==1):
		Fib.append(1)
	print(Fib[i])
	
