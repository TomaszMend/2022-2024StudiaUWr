n=int(input("Który element ciągu? : "))
a=1
q=2
def ciaggeo(n,a,q):
    for x in range(n):
        a=a*q;
    print(a)
ciaggeo(n,a,q)
