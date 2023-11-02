import numpy
from disable_warning import disable_warnings as dw

A = set(numpy.arange(1,10,2)) 
B = set(numpy.arange(0,10,2))

dw()
print(A, B)