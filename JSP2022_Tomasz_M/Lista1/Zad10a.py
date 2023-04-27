import cmath
z=complex(input())
s=cmath.sin(z)
c=cmath.cos(z)

print(s.real, s.imag)
print(c.real, c.imag)

print("Dodaje sin^2(z) do cos^2(z)")
print(s**2 + c**2)
if (s**2 + c**2 == 1):
    print("sin^2(z) do cos^2(z) wynosi 1")
else:
    print("Nope! It ain't working.")
