with open("PESEL.txt") as file:
    pesele = [line.rstrip() for line in file]
for x in range(10):
    slowo=pesele[x]
    suma=0
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
    if int(slowo[10])==k:
        print("Pesel jest poprawnie skonstruowany")
        year2=slowo[0:2]
        month=slowo[2:4]
        day=slowo[4:6]
        if int(month)>80:
            year1="18"
            month=str(int(month)-80)
            if len(month)==1:
                month="0"+month
        elif int(month)>60:
            year1="22"
            month=str(int(month)-60)
            if len(month)==1:
                month="0"+month
        elif int(month)>40:
            year1="21"
            month=str(int(month)-40)
            if len(month)==1:
                month="0"+month
        elif int(month)>20:
            year1="20"
            month=str(int(month)-20)
            if len(month)==1:
                month="0"+month
        else:
            year1="19"
        if int(slowo[9])%2==0:
            plec="Kobieta"
        else:
            plec="Mężczyzna"
        
    else:
        print("pesel nie jest poprawnie skonstuowany")
    with open('PESEL_sprawdzone.txt', 'a') as f:
        f.write("nr PESEL: %s \n Data Urodznia: %s.%s.%s; \t płeć: %s \n" % (slowo,day,month,year1+year2,plec))
