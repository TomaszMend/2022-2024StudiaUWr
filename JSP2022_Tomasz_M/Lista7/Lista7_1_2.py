import time
import sys
def Fib(n):
    if n == 1:
        return 0;
    elif n == 2:
        return 1;
    else:
        return int(Fib(n-1)+Fib(n-2));
N=int(input("Do którego wyrazu Fibonacciego: "))
start = time.time()
for x in range(1,N+1):
    print(Fib(x))
print(time.time()-start)
