
def romantoarabic(x):
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    arab = 0
    if (len(x) == 1) :
        arab =+ roman[x]
    else:
        i=0
        while i < len(x)-1:
            if x[i] < x[i+1]:
                arab = arab + roman[x[i+1]] - roman[x[i]];
                i = i + 2
            else:
                arab = arab + roman[x[i]]
                i = i + 1
    return arab
rzym=input("Wpisz liczbę rzymską (proszę umieścić na końcu spacje): ")
print("Twoja liczba to ", romantoarabic(rzym))
