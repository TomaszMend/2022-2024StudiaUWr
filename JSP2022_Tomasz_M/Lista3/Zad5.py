import re
haslo = input("Wpisz swoje nowe haslo  ")
if re.search(r"[a-z]", haslo) and re.search(r"[A-Z]", haslo) and re.search(r"[0-9]", haslo) and re.search(r"[$#@]", haslo) and len(haslo)>6 and len(haslo)<16:
	print("Twoje haslo spelnia wymagania")
else:
	print("Twoje haslo nie spelnia wymagan")
