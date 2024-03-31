import numpy as np
from matrix33 import MatrixHashAndCache


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[1, 3], [4, 2]])
D = np.array([[5, 6], [7, 8]])

hasher = MatrixHashAndCache()

with open("HW3/artifacts/3.3/A.txt", "w") as f:
    f.write(str(A))
with open("HW3/artifacts/3.3/B.txt", "w") as f:
    f.write(str(B))
with open("HW3/artifacts/3.3/C.txt", "w") as f:
    f.write(str(C))
with open("HW3/artifacts/3.3/D.txt", "w") as f:
    f.write(str(D))

AB = hasher.get_cache(A, B)
with open("HW3/artifacts/3.3/AB.txt", "w") as f:
    f.write(str(AB))
CD = hasher.get_cache(C, D)
with open("HW3/artifacts/3.3/CD.txt", "w") as f:
    f.write(str(CD))

hash_AB = hasher.__hash__(AB)
hash_CD = hasher.__hash__(CD)
with open("HW3/artifacts/3.3/hash.txt", "w") as f:
    f.write(str(hash_AB) + "\n")
    f.write(str(hash_CD) + "\n")