
sam = ["a","e","i","o","u","y","ą","ę","ó"]
lit = input("Podaj literę: ")
lit = lit.lower()
if lit in sam:
	print("Podana litera jest samogłoską")
else:
	print("Podana litera jest współgłoską")

