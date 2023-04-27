import numpy

obliczenia=numpy.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
wyniki=numpy.array([6,2,-5,17,12])
rownania=numpy.linalg.solve(obliczenia,wyniki)
print("\n","x równa się: ","%.2f" % rownania[0],"\n","y równa się: ","%.2f" % rownania[1],"\n","z równa się: ","%.2f" % rownania[2],"\n","t równa się: ","%.2f" % rownania[3],"\n","u równa się: ","%.2f" % rownania[4],"\n")
