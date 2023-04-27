import random
calytekst=""
for x in range(10):
    slowo=""
    suma=0
    for m in range(3):
        slowo=slowo+str(random.randint(0, 9))
    if slowo[2]=="9" or slowo[2]=="7" or slowo[2]=="5" or slowo[2]=="3" or slowo[2]=="1":
        slowo=slowo+str(random.randint(0, 2))
    elif slowo[2]=="8" or slowo[2]=="6" or slowo[2]=="4" or slowo[2]=="2" or slowo[2]=="0":
        slowo=slowo+str(random.randint(1, 9))
    else:
        slowo=slowo+str(random.randint(0, 9))
    month=slowo[2:]
    if int(month)>80:
        year1="18"
        month=int(month)-80
    elif int(month)>60:
        year1="22"
        month=int(month)-60
    elif int(month)>40:
        year1="21"
        month=int(month)-40
    elif int(month)>20:
        year1="20"
        month=int(month)-20
    else:
        year1="19"
    year=int(year1+slowo[0:2])
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        slowo=slowo+str(random.randint(0,3))
        if int(slowo[4])==3:
            slowo=slowo+str(random.randint(0,1))
        elif int(slowo[4])==0:
            slowo=slowo+str(random.randint(1,9))
        else:
            slowo=slowo+str(random.randint(0,9))
    elif month==2:
        if year%4==0:
                slowo=slowo+str(random.randint(0,2))
                slowo=slowo+str(random.randint(0,9))
        else:
                slowo=slowo+str(random.randint(0,2))
                if int(slowo[4])==2:
                    slowo=slowo+str(random.randint(0,8))
                elif int(slowo[4])==0:
                    slowo=slowo+str(random.randint(1,9))
                else:
                    slowo=slowo+str(random.randint(0,9))
    else:
        slowo=slowo+str(random.randint(0,3))
        if int(slowo[4])==3:
            slowo=slowo+"0"
        elif int(slowo[4])==0:
            slowo=slowo+str(random.randint(1,9))
        else:
            slowo=slowo+str(random.randint(0,9))
    for m in range(4):
        k=str(random.randint(0, 9))
        slowo=slowo+k
    for m in range(10):
        p=1
        if m%2==0:
            p=3
        if m%3==0:
            p=7
        if m%4==0:
            p=9
        if len(slowo[m]*p)>2:
            k=str(slowo[m]*p)
            suma=suma+int(k[len(k)-1])
        else:
            suma=suma+int(slowo[m]*p)
    if suma>9:
        suma=str(suma)[len(str(suma))-1]
    k=10-int(suma)
    if k==10:
        k=0
    slowo=slowo+str(k)
    calytekst=calytekst+slowo+"\n"
with open('PESEL.txt', 'w') as f:
    f.write(calytekst)
