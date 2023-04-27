import math
x=int(input("Wpisz stopnie: "))
y=int(input("Wpisz radiany: "))
def radtodegrees(x):
  print('%.2f' % math.radians(x))
def degreestorad(y):
  print('%.2f' % math.degrees(y))
radtodegrees(x)
degreestorad(y)