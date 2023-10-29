import numpy as np

A = set(np.arange(10))

B = (set(np.arange(0,10,3)))

bla = {1,5,9}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

print(bla.difference(A.difference(B)))
