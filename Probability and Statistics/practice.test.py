import numpy

from disable_warning.dw import dw

A = set(numpy.arange(1,10,2)) 
B = set(numpy.arange(0,10,2))
C = set(numpy.arange(0,10,3))
print(A, B, C)

print("\nUnions")
print(A.union(B))
print(A.union(C))

print("\nIntersections")
print(f"{A.intersection(C)} {B.intersection(C)}")

print("\nDifference")
print(f"{A.difference(C)}")

print("\nTest.")
print(f"A:{A}, C: {C}")
print(f"\nUnion: {A.union(C)}, Intersection: {A.intersection(C)}, Difference: {A.difference(C)}")