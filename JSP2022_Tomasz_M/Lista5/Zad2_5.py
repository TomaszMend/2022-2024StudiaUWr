#https://www.geeksforgeeks.org/python-convert-numeric-words-to-numbers/
def słowowliczbe(x):
    listaliczb = {'jeden': '1','dwa': '2','trzy': '3','cztery': '4','pięć': '5','sześć': '6','siedem': '7','osiem': '8','dziewięć': '9','zero': '0'}
    return ''.join(listaliczb[m] for m in x.split())
print("Wpisz słownie liczbę (w taki sposób: jeden dwa jeden zero to będzie 1210): ")
liczs = input()
print(słowowliczbe(liczs))