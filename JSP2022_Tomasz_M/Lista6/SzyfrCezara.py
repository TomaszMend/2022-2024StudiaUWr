def szyfr(n,tekst):
    lista={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    list={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    x=""
    for i in range(0,len(tekst)):
        if tekst[i] in "!@#$%^&*()_+-=[]{};':,./<>?1234567890ĄąŚśĆćĘęóÓŁłżŻźŹ ":
            x=x+tekst[i]
        elif list[tekst[i].upper()]+n>25:
            p=list[tekst[i].upper()]+n-26
            if tekst[i].isupper():
                x=x+lista[p].upper()
            elif tekst[i].islower():
                x=x+lista[p].lower()
        else:
            if tekst[i].isupper():
                x=x+lista[list[tekst[i]]+n].upper()
            elif tekst[i].islower():
                x=x+lista[list[tekst[i].upper()]+n].lower()
    return x;
def deszyfr(n,tekst):
    lista={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    list={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    x=""
    for i in range(0,len(tekst)):
        if tekst[i] in "!@#$%^&*()_+-=[]{};':,./<>?1234567890ĄąŚśĆćĘęóÓŁłżŻźŹ ":
            x=x+tekst[i]
        elif list[tekst[i].upper()]-n<0:
            p=26+list[tekst[i].upper()]-n
            if tekst[i].isupper():
                x=x+lista[p].upper()
            elif tekst[i].islower():
                x=x+lista[p].lower()
        else:
            if tekst[i].isupper():
                x=x+lista[list[tekst[i]]-n].upper()
            elif tekst[i].islower():
                x=x+lista[list[tekst[i].upper()]-n].lower()
    return x;
