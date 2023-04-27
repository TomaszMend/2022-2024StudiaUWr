def słowawliczby(liczs):
    licz = 0
    if "pięćdziesiąt" in liczs:
        if len("pięćdziesiąt") == len(liczs):
            licz = 50
        if "jeden" in liczs:
            licz = 51
        if "dwa" in liczs:
            licz = 52
        if "trzy" in liczs:
            licz = 53
        if "cztery" in liczs:
            licz = 54
        if liczs.count("pięć") == 2:
            licz = 55
        if "sześć" in liczs:
            licz = 56
        if "siedem" in liczs:
            licz = 57
        if "osiem" in liczs:
            licz = 58
        if "dziewięć" in liczs:
            licz = 59
    if "czterdzieści" in liczs:
        if len("czterdzieści") == len(liczs):
            licz = 40
        if "jeden" in liczs:
            licz = 41
        if "dwa" in liczs:
            licz = 42
        if "trzy" in liczs:
            licz = 43
        if "cztery" in liczs:
            licz = 44
        if "pięć" in liczs:
            licz = 45
        if "sześć" in liczs:
            licz = 46
        if "siedem" in liczs:
            licz = 47
        if "osiem" in liczs:
            licz = 48
        if "dziewięć" in liczs:
            licz = 49
    if "trzydzieści" in liczs:
        if len("trzydzieści") == len(liczs):
            licz = 30
        if "jeden" in liczs:
            licz = 31
        if "dwa" in liczs:
            licz = 32
        if liczs.count("trzy") == 2:
            licz = 33
        if "cztery" in liczs:
            licz = 34
        if "pięć" in liczs:
            licz = 35
        if "sześć" in liczs:
            licz = 36
        if "siedem" in liczs:
            licz = 37
        if "osiem" in liczs:
            licz = 38
        if "dziewięć" in liczs:
            licz = 39
    if "dwadzieścia" in liczs:
        if len("dwadzieścia") == len(liczs):
            licz = 20
        if "jeden" in liczs:
            licz = 21
        if liczs.count("dwa") == 2:
            licz = 22
        if "trzy" in liczs:
            licz = 23
        if "cztery" in liczs:
            licz = 24
        if "pięć" in liczs:
            licz = 25
        if "sześć" in liczs:
            licz = 26
        if "siedem" in liczs:
            licz = 27
        if "osiem" in liczs:
            licz = 28
        if "dziewięć" in liczs:
            licz = 29
    if "naście" in liczs:
        if "jeden" in liczs:
            licz = 11
        if "dwa" in liczs:
            licz = 12
        if "trzy" in liczs:
            licz = 13
        if "czter" in liczs:
            licz = 14
        if "pięt" in liczs:
            licz = 15
        if "szes" in liczs:
            licz = 16
        if "siedem" in liczs:
            licz = 17
        if "osiem" in liczs:
            licz = 18
        if "dziewięt" in liczs:
            licz = 19
    if "dzisięć" in liczs:
        licz = 10
    if licz == 0:
        if "jeden" in liczs:
            licz = 1
        if "dwa" in liczs:
            licz = 2
        if "trzy" in liczs:
            licz = 3
        if "cztery" in liczs:
            licz = 4
        if "pięć" in liczs:
            licz = 5
        if "sześć" in liczs:
            licz = 6
        if "siedem" in liczs:
            licz = 7
        if "osiem" in liczs:
            licz = 8
        if "dziewięć" in liczs:
            licz = 9
    return licz

print("Wpisz słownie liczbe od 1 do 59")
liczs=input()
print("Wpisana liczba to ",słowawliczby(liczs))
