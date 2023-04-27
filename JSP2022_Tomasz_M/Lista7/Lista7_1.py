import time
import sys
N=int(input("Do którego wyrazu Fibonacciego: "))
start = time.time()
a=0
b=1
if(N==0) or (N>0):
    print(a)
if(N==1) or (N>1):
    print(b)
if(N>1):
    for x in range(1,N-1):
        if(x%2==0):
            a=a+b
        else:
            b=a+b
        print(a+b)
print(time.time()-start)